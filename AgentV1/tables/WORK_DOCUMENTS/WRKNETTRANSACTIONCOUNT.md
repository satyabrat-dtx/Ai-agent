# DB2ADMIN.WRKNETTRANSACTIONCOUNT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 239604

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `ENTITYDOCNAME` | VARCHAR(270) |  |  |  |  |
| 4 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 5 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 6 | `DOCTEMPLATECODE` | CHAR(8) |  |  |  |  |
| 7 | `DOCTEMPLATENAME` | VARCHAR(1000) |  |  |  |  |
| 8 | `PERIODNOS` | DECIMAL(10,5) |  |  |  |  |
| 9 | `TODAYNOS` | DECIMAL(10,5) |  |  |  |  |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKNETTRANSACTIONCOUNTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.ENTITYDOCNAME,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.DOCTEMPLATECODE,
       t.DOCTEMPLATENAME,
       t.PERIODNOS,
       t.TODAYNOS,
       t.ABSUNIQUEID
FROM   DB2ADMIN.WRKNETTRANSACTIONCOUNT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
