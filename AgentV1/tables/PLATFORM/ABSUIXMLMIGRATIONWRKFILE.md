# DB2ADMIN.ABSUIXMLMIGRATIONWRKFILE

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `ABSUIXMLATTRABSUIXMLPATH`, `ABSUIXMLATTRABSUIXMLNAME`, `ABSUIXMLATTRNAME`, `USERUSERID`, `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 115744

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSUIXMLATTRABSUIXMLPATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `ABSUIXMLATTRABSUIXMLNAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 2 | `ABSUIXMLATTRNAME` | VARCHAR(120) | NOT NULL | PK | primary_key |  |
| 3 | `USERUSERID` | CHAR(25) | NOT NULL | PK | primary_key |  |
| 4 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 5 | `CUSTOMOBJSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 6 | `ORIGINALOBJSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 7 | `PREVIOUSOBJSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 8 | `PREVIOUSATTRNAME` | VARCHAR(120) |  |  |  |  |
| 9 | `PREVIOUSNOHIDEOBJSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 10 | `PREVIOUSNOHIDEATTRNAME` | VARCHAR(120) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ABSUIXMLATTRABSUIXMLPATH,
       t.ABSUIXMLATTRABSUIXMLNAME,
       t.ABSUIXMLATTRNAME,
       t.USERUSERID,
       t.COMPANYCODE,
       t.CUSTOMOBJSEQUENCE,
       t.ORIGINALOBJSEQUENCE,
       t.PREVIOUSOBJSEQUENCE,
       t.PREVIOUSATTRNAME,
       t.PREVIOUSNOHIDEOBJSEQUENCE,
       t.PREVIOUSNOHIDEATTRNAME
FROM   DB2ADMIN.ABSUIXMLMIGRATIONWRKFILE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
