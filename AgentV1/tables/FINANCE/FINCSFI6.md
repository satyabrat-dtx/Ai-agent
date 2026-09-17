# DB2ADMIN.FINCSFI6

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `URSVAR`, `URSCONF`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 103781

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(8) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(8) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `URSVAR` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 3 | `URSCONF` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 4 | `URSTXT` | CHAR(50) |  |  |  |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINCSFI6UID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.URSVAR,
       t.URSCONF,
       t.URSTXT,
       t.ABSUNIQUEID
FROM   DB2ADMIN.FINCSFI6 t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
