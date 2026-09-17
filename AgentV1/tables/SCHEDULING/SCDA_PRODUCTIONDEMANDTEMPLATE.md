# DB2ADMIN.SCDA_PRODUCTIONDEMANDTEMPLATE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `IDENTIFIER`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 184657

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CODE` | VARCHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 3 | `HANDLEDBYMQM` | CHAR(1) |  |  |  |  |
| 4 | `HANDLEDBYMCM` | CHAR(1) |  |  |  |  |
| 5 | `SERVEDCODETABLENAME` | VARCHAR(30) |  |  |  |  |
| 6 | `SERVEDCODECOLUMNAME` | VARCHAR(30) |  |  |  |  |
| 7 | `SERVINGCODETABLENAME` | VARCHAR(30) |  |  |  |  |
| 8 | `SERVINGCODECOLUMNAME` | VARCHAR(30) |  |  |  |  |
| 9 | `SERVINGCODEDEFNITION` | CHAR(1) |  |  |  |  |
| 10 | `SERVEDCODEDEFNITION` | CHAR(1) |  |  |  |  |
| 11 | `ITEMTYPESERVED` | VARCHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IDENTIFIER,
       t.CODE,
       t.SHORTDESCRIPTION,
       t.HANDLEDBYMQM,
       t.HANDLEDBYMCM,
       t.SERVEDCODETABLENAME,
       t.SERVEDCODECOLUMNAME,
       t.SERVINGCODETABLENAME,
       t.SERVINGCODECOLUMNAME,
       t.SERVINGCODEDEFNITION,
       t.SERVEDCODEDEFNITION,
       t.ITEMTYPESERVED
FROM   DB2ADMIN.SCDA_PRODUCTIONDEMANDTEMPLATE t
FETCH FIRST 100 ROWS ONLY;
```
