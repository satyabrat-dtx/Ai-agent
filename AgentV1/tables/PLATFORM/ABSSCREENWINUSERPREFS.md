# DB2ADMIN.ABSSCREENWINUSERPREFS

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `FUNCTIONID`, `REVISION`, `SCREENWINCODE`, `COMPANYCODE`, `USERID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 194299

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FUNCTIONID` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 1 | `REVISION` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 2 | `SCREENWINCODE` | CHAR(30) | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `USERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 5 | `MDICONFIGURATION` | CLOB(1000000) |  |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSSCREENWINUSERPREFSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FUNCTIONID,
       t.REVISION,
       t.SCREENWINCODE,
       t.COMPANYCODE,
       t.USERID,
       t.MDICONFIGURATION,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSSCREENWINUSERPREFS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
