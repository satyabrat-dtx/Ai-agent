# DB2ADMIN.WRKABSAUTHORISATIONSPRINT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `IDENTIFIER`, `COMPANYCODE`, `USERUSERID`, `UIXMLPATH`, `UIXMLNAME`, `RECORDTYPE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 206933

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IDENTIFIER` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `USERUSERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `UIXMLPATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 4 | `UIXMLNAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 5 | `RECORDTYPE` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `CODE` | CHAR(50) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 7 | `ISGROUP` | SMALLINT | NOT NULL |  |  |  |
| 8 | `DESCRIPTION` | VARCHAR(250) |  |  | description |  |
| 9 | `CREATEAUTH` | INTEGER | NOT NULL |  |  |  |
| 10 | `UPDATEAUTH` | INTEGER | NOT NULL |  |  |  |
| 11 | `DELETEAUTH` | INTEGER | NOT NULL |  |  |  |
| 12 | `QUERYAUTH` | INTEGER | NOT NULL |  |  |  |
| 13 | `READAUTH` | INTEGER | NOT NULL |  |  |  |
| 14 | `SUBMITAUTH` | INTEGER | NOT NULL |  |  |  |
| 15 | `USEALLOWED` | INTEGER | NOT NULL |  |  |  |
| 16 | `PRINTALLOWED` | INTEGER | NOT NULL |  |  |  |
| 17 | `PATTERNTYPE` | INTEGER | NOT NULL |  |  |  |
| 18 | `UIXMLREPLACEDPATH` | VARCHAR(50) |  |  |  |  |
| 19 | `UIXMLREPLACEDNAME` | VARCHAR(54) |  |  |  |  |
| 20 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL |  | audit |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IDENTIFIER,
       t.COMPANYCODE,
       t.USERUSERID,
       t.UIXMLPATH,
       t.UIXMLNAME,
       t.RECORDTYPE,
       t.CODE,
       t.ISGROUP,
       t.DESCRIPTION,
       t.CREATEAUTH,
       t.UPDATEAUTH,
       t.DELETEAUTH
FROM   DB2ADMIN.WRKABSAUTHORISATIONSPRINT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
