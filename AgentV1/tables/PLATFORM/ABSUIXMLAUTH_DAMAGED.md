# DB2ADMIN.ABSUIXMLAUTH_DAMAGED

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `ABSUIXMLPATH`, `ABSUIXMLNAME`, `USERUSERID`, `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 19238

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSUIXMLPATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `ABSUIXMLNAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 2 | `USERUSERID` | CHAR(25) | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `CREATEAUTH` | SMALLINT | NOT NULL |  |  |  |
| 5 | `READAUTH` | SMALLINT | NOT NULL |  |  |  |
| 6 | `UPDATEAUTH` | SMALLINT | NOT NULL |  |  |  |
| 7 | `DELETEAUTH` | SMALLINT | NOT NULL |  |  |  |
| 8 | `QUERYAUTH` | SMALLINT | NOT NULL |  |  |  |
| 9 | `SUBMITAUTH` | SMALLINT | NOT NULL |  |  |  |
| 10 | `READASDEFAULT` | SMALLINT | NOT NULL |  |  |  |
| 11 | `CREATEEQBALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `COLLECTIONDEFAULTEQBCODE` | CHAR(30) |  |  |  |  |
| 13 | `LOOKUPDEFAULTEQBCODE` | CHAR(30) |  |  |  |  |
| 14 | `CREATEGBALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 15 | `DEFAULTGBCODE` | CHAR(30) |  |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ABSUIXMLPATH,
       t.ABSUIXMLNAME,
       t.USERUSERID,
       t.COMPANYCODE,
       t.CREATEAUTH,
       t.READAUTH,
       t.UPDATEAUTH,
       t.DELETEAUTH,
       t.QUERYAUTH,
       t.SUBMITAUTH,
       t.READASDEFAULT,
       t.CREATEEQBALLOWED
FROM   DB2ADMIN.ABSUIXMLAUTH_DAMAGED t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
