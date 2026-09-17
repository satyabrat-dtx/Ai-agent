# DB2ADMIN.PROJECTPLANNING

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 70888

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(20) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `PLANNERANNOTATION` | VARCHAR(250) |  |  |  |  |
| 3 | `PLANRUNNING` | SMALLINT | NOT NULL |  |  |  |
| 4 | `CANBEEXPLODED` | SMALLINT | NOT NULL |  |  |  |
| 5 | `PLANNINGTEMPLATECODE` | CHAR(8) |  |  |  |  |
| 6 | `PROGRESSSTATUS` | INTEGER | NOT NULL |  |  |  |
| 7 | `LINESCHANGED` | SMALLINT | NOT NULL |  |  |  |
| 8 | `ERRORS` | VARCHAR(960) |  |  |  |  |
| 9 | `TRACECREATIONID` | DECIMAL(11,0) |  |  |  |  |
| 10 | `TRACELINE` | INTEGER | NOT NULL |  |  |  |
| 11 | `SUBMITTEDJOBJOBNUMBER` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.PLANNERANNOTATION,
       t.PLANRUNNING,
       t.CANBEEXPLODED,
       t.PLANNINGTEMPLATECODE,
       t.PROGRESSSTATUS,
       t.LINESCHANGED,
       t.ERRORS,
       t.TRACECREATIONID,
       t.TRACELINE,
       t.SUBMITTEDJOBJOBNUMBER
FROM   DB2ADMIN.PROJECTPLANNING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
