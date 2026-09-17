# DB2ADMIN.WRKFORM3A

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `EMPLOYEEIDCODE`, `MONTHCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 164385

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `EMPLOYEEIDCODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 3 | `MONTHCODE` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `PFACCOUNTNO` | CHAR(15) |  |  |  |  |
| 5 | `FIRSTNAME` | CHAR(25) |  |  |  |  |
| 6 | `MIDDLENAME` | CHAR(25) |  |  |  |  |
| 7 | `LASTNAME` | CHAR(25) |  |  |  |  |
| 8 | `MINEMPLOYEETOEPF` | DECIMAL(5,2) |  |  |  |  |
| 9 | `MINEMPLOYERTOEPF` | DECIMAL(5,2) |  |  |  |  |
| 10 | `FATHERNAME` | CHAR(30) |  |  |  |  |
| 11 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 12 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 13 | `WAGESAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 14 | `WORKEREPF` | DECIMAL(17,2) |  |  |  |  |
| 15 | `EMPLOYEREPF` | DECIMAL(17,2) |  |  |  |  |
| 16 | `EMPLOYEREPS` | DECIMAL(17,2) |  |  |  |  |
| 17 | `MONTH` | CHAR(7) |  |  |  |  |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFORM3AUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.EMPLOYEEIDCODE,
       t.MONTHCODE,
       t.PFACCOUNTNO,
       t.FIRSTNAME,
       t.MIDDLENAME,
       t.LASTNAME,
       t.MINEMPLOYEETOEPF,
       t.MINEMPLOYERTOEPF,
       t.FATHERNAME,
       t.FROMDATE
FROM   DB2ADMIN.WRKFORM3A t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
