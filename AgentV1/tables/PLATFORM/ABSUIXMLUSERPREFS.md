# DB2ADMIN.ABSUIXMLUSERPREFS

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `PATH`, `NAME`, `COMPANYCODE`, `USERID`, `TOKEN`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 194378

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `NAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `USERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 4 | `TOKEN` | VARCHAR(60) | NOT NULL | PK | primary_key |  |
| 5 | `WIDTH` | INTEGER | NOT NULL |  |  |  |
| 6 | `HEIGHT` | INTEGER | NOT NULL |  |  |  |
| 7 | `POSX` | INTEGER | NOT NULL |  |  |  |
| 8 | `POSY` | INTEGER | NOT NULL |  |  |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSUIXMLUSERPREFSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PATH,
       t.NAME,
       t.COMPANYCODE,
       t.USERID,
       t.TOKEN,
       t.WIDTH,
       t.HEIGHT,
       t.POSX,
       t.POSY,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSUIXMLUSERPREFS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
