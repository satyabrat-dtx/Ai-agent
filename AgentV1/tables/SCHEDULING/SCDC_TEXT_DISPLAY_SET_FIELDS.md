# DB2ADMIN.SCDC_TEXT_DISPLAY_SET_FIELDS

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `TDF_IDENTIFIER`, `TDF_WORKSTATION`, `TDF_SET_NAME`, `TDF_SET_TYPE`, `TDF_FIELD`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189489

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TDF_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `TDF_WORKSTATION` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 2 | `TDF_SET_NAME` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `TDF_SET_TYPE` | VARCHAR(14) | NOT NULL | PK | primary_key |  |
| 4 | `TDF_FIELD` | SMALLINT | NOT NULL | PK | primary_key |  |
| 5 | `TDF_TITLE` | VARCHAR(50) |  |  |  |  |
| 6 | `TDF_ORG_TITLE` | VARCHAR(50) |  |  |  |  |
| 7 | `TDF_CHECKED` | SMALLINT |  |  |  |  |
| 8 | `TDF_FROMPOS` | SMALLINT |  |  |  |  |
| 9 | `TDF_TOPOS` | SMALLINT |  |  |  |  |
| 10 | `TDF_FIELDNAME` | VARCHAR(30) |  |  |  |  |
| 11 | `TDF_PROPERTY` | VARCHAR(5) |  |  |  |  |
| 12 | `TDF_LINE_SEQ` | SMALLINT |  |  |  |  |
| 13 | `TDF_LINE_NUMBER` | SMALLINT |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.TDF_IDENTIFIER,
       t.TDF_WORKSTATION,
       t.TDF_SET_NAME,
       t.TDF_SET_TYPE,
       t.TDF_FIELD,
       t.TDF_TITLE,
       t.TDF_ORG_TITLE,
       t.TDF_CHECKED,
       t.TDF_FROMPOS,
       t.TDF_TOPOS,
       t.TDF_FIELDNAME,
       t.TDF_PROPERTY
FROM   DB2ADMIN.SCDC_TEXT_DISPLAY_SET_FIELDS t
FETCH FIRST 100 ROWS ONLY;
```
