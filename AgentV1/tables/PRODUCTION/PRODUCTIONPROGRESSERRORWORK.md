# DB2ADMIN.PRODUCTIONPROGRESSERRORWORK

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 105973

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `PRODELEMDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 5 | `PRODELEMDEMANDCODE` | CHAR(15) |  |  |  |  |
| 6 | `PRODELEMITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 7 | `PRODELEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 8 | `PRODELEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 10 | `PRODSTEPPRODEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 11 | `PRODSTEPPRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 12 | `PRODSTEPSTEPNUMBER` | DECIMAL(5,0) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PROPROGRESSERRORWORKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.COMPANYCODE,
       t.PRODELEMDEMANDCOUNTERCODE,
       t.PRODELEMDEMANDCODE,
       t.PRODELEMITEMTYPEAFICODE,
       t.PRODELEMELEMENTSUBCODEKEY,
       t.PRODELEMELEMENTCODE,
       t.ABSUNIQUEID,
       t.PRODSTEPPRODEMANDCOUNTERCODE,
       t.PRODSTEPPRODUCTIONDEMANDCODE
FROM   DB2ADMIN.PRODUCTIONPROGRESSERRORWORK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
