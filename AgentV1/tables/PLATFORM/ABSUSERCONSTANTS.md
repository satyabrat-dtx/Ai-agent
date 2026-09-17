# DB2ADMIN.ABSUSERCONSTANTS

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `USERUSERID`, `COMPANYCODE`, `USERKEY`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 10265

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `USERUSERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `USERKEY` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `VALUE` | CHAR(50) | NOT NULL |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSUSERCONSTANTSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.USERUSERID,
       t.COMPANYCODE,
       t.USERKEY,
       t.VALUE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSUSERCONSTANTS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
