# DB2ADMIN.INSURANCETRANSACTIONHEADER

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `EMPLOYEEIDCODE`, `INSURANCEAGENTCODEICSTABLECODE`, `INSURANCEAGENTCODECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 167027

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `INSURANCEAGENTCODEICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `INSURANCEAGENTCODECODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `INSURANCESERIALNUMBER` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 5 | `INSURANCEDATE` | DATE | NOT NULL |  |  |  |
| 6 | `INSURANCEEXPIRYDATE` | DATE | NOT NULL |  |  |  |
| 7 | `POLICYNUMBER` | CHAR(25) | NOT NULL |  |  |  |
| 8 | `NOOFINSTALMENTS` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 9 | `INSURANCEAMOUNT` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 10 | `INSURANCEPREMIUMAMT` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 11 | `UPTODATEPAIDAMT` | DECIMAL(17,2) |  |  |  |  |
| 12 | `STOPDEDUCTION` | SMALLINT | NOT NULL |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `INSURANCETRANSACTIONHEADER.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `INSURANCETRANSACTIONHEADER.COMPANYCODE = EMPLOYEE.COMPANYCODE AND INSURANCETRANSACTIONHEADER.EMPLOYEEIDCODE = EMPLOYEE.CODE` |
| `ICSENTITY_INSURANCEAGENTCODE` | `COMPANYCODE`, `INSURANCEAGENTCODEICSTABLECODE`, `INSURANCEAGENTCODECODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `INSURANCETRANSACTIONHEADER.COMPANYCODE = ICSENTITY.COMPANYCODE AND INSURANCETRANSACTIONHEADER.INSURANCEAGENTCODEICSTABLECODE = ICSENTITY.ICSTABLECODE AND INSURANCETRANSACTIONHEADER.INSURANCEAGENTCODECODE = ICSENTITY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INSURANCETRANSACTIONHEADERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.INSURANCEAGENTCODEICSTABLECODE,
       t.INSURANCEAGENTCODECODE,
       t.INSURANCESERIALNUMBER,
       t.INSURANCEDATE,
       t.INSURANCEEXPIRYDATE,
       t.POLICYNUMBER,
       t.NOOFINSTALMENTS,
       t.INSURANCEAMOUNT,
       t.INSURANCEPREMIUMAMT,
       t.UPTODATEPAIDAMT
FROM   DB2ADMIN.INSURANCETRANSACTIONHEADER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
