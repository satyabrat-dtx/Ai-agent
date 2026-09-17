# DB2ADMIN.TEMPFMGSETTLEMENT

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 28
- **Primary key**: `AUTONUMBER`, `SNO`, `COMPANYCODE`, `EMPLOYEEIDCODE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 168882

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `AUTONUMBER` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 1 | `SNO` | BIGINT | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `FMGCODEFMGCODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `ASSETCODE` | CHAR(10) | NOT NULL |  |  |  |
| 5 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `SETTLEMENTDATE` | DATE |  |  |  |  |
| 7 | `SERIALNUMBER` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 8 | `ASSETVALUE` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 9 | `APPROVEDBYCODE` | CHAR(9) |  | FK | foreign_key |  |
| 10 | `ISSUEDATE` | DATE | NOT NULL |  |  |  |
| 11 | `DUEDATE` | DATE |  |  |  |  |
| 12 | `WDVAPPLICABLE` | INTEGER | NOT NULL |  |  |  |
| 13 | `RETURNDATE` | DATE |  |  |  |  |
| 14 | `DEPERICATIONPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 15 | `SELLBILLAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 22 | `SETMNTAPPROVEDBYCODE` | CHAR(9) |  | FK | foreign_key |  |
| 23 | `SETTLEMENTAPPROVEDDATE` | DATE |  |  |  |  |
| 24 | `PAIDAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 25 | `PAYEMENTTRROUGH` | INTEGER | NOT NULL |  |  |  |
| 26 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TEMPFMGSETTLEMENT.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_APPROVEDBY` | `COMPANYCODE`, `APPROVEDBYCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `TEMPFMGSETTLEMENT.COMPANYCODE = EMPLOYEE.COMPANYCODE AND TEMPFMGSETTLEMENT.APPROVEDBYCODE = EMPLOYEE.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `TEMPFMGSETTLEMENT.COMPANYCODE = EMPLOYEE.COMPANYCODE AND TEMPFMGSETTLEMENT.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `EMPLOYEE_SETMNTAPPROVEDBY` | `COMPANYCODE`, `SETMNTAPPROVEDBYCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `TEMPFMGSETTLEMENT.COMPANYCODE = EMPLOYEE.COMPANYCODE AND TEMPFMGSETTLEMENT.SETMNTAPPROVEDBYCODE = EMPLOYEE.CODE` |
| `FMGMASTER_FMGCODE` | `COMPANYCODE`, `FMGCODEFMGCODE` | [`FMGMASTER`](../HR/FMGMASTER.md) | `COMPANYCODE`, `FMGCODE` | RESTRICT | `TEMPFMGSETTLEMENT.COMPANYCODE = FMGMASTER.COMPANYCODE AND TEMPFMGSETTLEMENT.FMGCODEFMGCODE = FMGMASTER.FMGCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TEMPFMGSETTLEMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.AUTONUMBER,
       t.SNO,
       t.COMPANYCODE,
       t.FMGCODEFMGCODE,
       t.ASSETCODE,
       t.EMPLOYEEIDCODE,
       t.SETTLEMENTDATE,
       t.SERIALNUMBER,
       t.ASSETVALUE,
       t.APPROVEDBYCODE,
       t.ISSUEDATE,
       t.DUEDATE
FROM   DB2ADMIN.TEMPFMGSETTLEMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
