# DB2ADMIN.ACCINSCLAIMREFENTRY

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `COMPANYCODE`, `EMPLOYEEIDCODE`, `ACCIDENTNOCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 164668

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ACCIDENTNOCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `POLICYNO` | CHAR(25) |  |  |  |  |
| 4 | `COMPANYNAME` | VARCHAR(200) |  |  |  |  |
| 5 | `CHEQUENO` | INTEGER | NOT NULL |  |  |  |
| 6 | `CHEQUEDATE` | DATE |  |  |  |  |
| 7 | `BANKNAME` | CHAR(30) |  |  |  |  |
| 8 | `OWNERNAME` | CHAR(100) |  |  |  |  |
| 9 | `COMPENSATION` | DECIMAL(10,0) |  |  |  |  |
| 10 | `MEDICAL` | DECIMAL(10,0) |  |  |  |  |
| 11 | `ADVANCEAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 12 | `ACTUALRECIEVEAMT` | DECIMAL(17,2) |  |  |  |  |
| 13 | `TOTALAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACCINTIMATION_ACCIDENTNO` | `COMPANYCODE`, `ACCIDENTNOCODE` | [`ACCINTIMATION`](../HR/ACCINTIMATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ACCINSCLAIMREFENTRY.COMPANYCODE = ACCINTIMATION.COMPANYCODE AND ACCINSCLAIMREFENTRY.ACCIDENTNOCODE = ACCINTIMATION.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ACCINSCLAIMREFENTRY.COMPANYCODE = COMPANY.CODE` |
| `EMPLOYEE_EMPLOYEEID` | `COMPANYCODE`, `EMPLOYEEIDCODE` | [`EMPLOYEE`](../HR/EMPLOYEE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ACCINSCLAIMREFENTRY.COMPANYCODE = EMPLOYEE.COMPANYCODE AND ACCINSCLAIMREFENTRY.EMPLOYEEIDCODE = EMPLOYEE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ACCINSCLAIMREFENTRYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EMPLOYEEIDCODE,
       t.ACCIDENTNOCODE,
       t.POLICYNO,
       t.COMPANYNAME,
       t.CHEQUENO,
       t.CHEQUEDATE,
       t.BANKNAME,
       t.OWNERNAME,
       t.COMPENSATION,
       t.MEDICAL,
       t.ADVANCEAMOUNT
FROM   DB2ADMIN.ACCINSCLAIMREFENTRY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
