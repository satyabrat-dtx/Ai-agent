# DB2ADMIN.SCDA_ARTICLE_TYPE

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `AT_IDENTIFIER`, `AT_ART_TYPE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 183696

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `AT_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `AT_ART_TYPE` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `AT_S_DESCR` | VARCHAR(28) |  |  |  |  |
| 3 | `AT_L_DESCR` | VARCHAR(60) |  |  |  |  |
| 4 | `AT_BALHANDLEDBYMQM` | CHAR(1) |  |  |  |  |
| 5 | `AT_ADDDATACOLUMNNAME` | VARCHAR(30) |  |  |  |  |
| 6 | `AT_PRODUCTTYPENATURE` | CHAR(1) |  |  |  |  |
| 7 | `AT_RESTIMEBEGINNING` | CHAR(1) |  |  |  |  |
| 8 | `AT_RESTIMEENDING` | CHAR(1) |  |  |  |  |
| 9 | `AT_LASTPRIMARYNR` | SMALLINT |  |  |  |  |
| 10 | `AT_MATERIAL_TOLLERANCE_CODE` | VARCHAR(6) |  |  |  |  |
| 11 | `AT_ISWARPTYPE` | CHAR(1) |  |  |  |  |
| 12 | `AT_HOURSTODOWNFROMMACHINE` | SMALLINT |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.AT_IDENTIFIER,
       t.AT_ART_TYPE,
       t.AT_S_DESCR,
       t.AT_L_DESCR,
       t.AT_BALHANDLEDBYMQM,
       t.AT_ADDDATACOLUMNNAME,
       t.AT_PRODUCTTYPENATURE,
       t.AT_RESTIMEBEGINNING,
       t.AT_RESTIMEENDING,
       t.AT_LASTPRIMARYNR,
       t.AT_MATERIAL_TOLLERANCE_CODE,
       t.AT_ISWARPTYPE
FROM   DB2ADMIN.SCDA_ARTICLE_TYPE t
FETCH FIRST 100 ROWS ONLY;
```
