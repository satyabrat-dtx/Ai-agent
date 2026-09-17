# DB2ADMIN.ABSSCREENDEFUSERPREFS

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `SCREENDEFFUNCTIONID`, `SCREENDEFREVISION`, `DOCKINGKEY`, `COMPANYCODE`, `USERID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 194257

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SCREENDEFFUNCTIONID` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 1 | `SCREENDEFREVISION` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `USERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 4 | `INITIALDOCKINGCONFIG` | CLOB(1000000) |  |  |  |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 6 | `DOCKINGKEY` | VARCHAR(70) | NOT NULL | PK | primary_key |  |
| 7 | `DOCKINGCONFIG` | CLOB(1000000) |  |  |  |  |
| 8 | `IGNORENEWDOCKINGCONFIG` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSSCREENDEFUSERPREFSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SCREENDEFFUNCTIONID,
       t.SCREENDEFREVISION,
       t.COMPANYCODE,
       t.USERID,
       t.INITIALDOCKINGCONFIG,
       t.ABSUNIQUEID,
       t.DOCKINGKEY,
       t.DOCKINGCONFIG,
       t.IGNORENEWDOCKINGCONFIG
FROM   DB2ADMIN.ABSSCREENDEFUSERPREFS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
