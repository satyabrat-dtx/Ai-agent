# DB2ADMIN.SCDC_AUTO_RUN_DEFINITION

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDC_')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `ARD_IDENTIFIER`, `ARD_WKST_CODE`, `ARD_AUTO_RUN_CODE`, `ARD_LINE_NUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 188530

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ARD_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `ARD_WKST_CODE` | VARCHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `ARD_AUTO_RUN_CODE` | VARCHAR(40) | NOT NULL | PK | primary_key |  |
| 3 | `ARD_LINE_NUMBER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 4 | `ARD_SEQUENCE` | SMALLINT |  |  |  |  |
| 5 | `ARD_OPERATION_CODE` | VARCHAR(2) |  |  |  |  |
| 6 | `ARD_BIN` | VARCHAR(40) |  |  |  |  |
| 7 | `ARD_GANTT` | VARCHAR(40) |  |  |  |  |
| 8 | `ARD_OPERATION_DETAILS` | VARCHAR(14) |  |  |  |  |
| 9 | `ARD_MAIL_GROUP_NAME` | VARCHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.ARD_IDENTIFIER,
       t.ARD_WKST_CODE,
       t.ARD_AUTO_RUN_CODE,
       t.ARD_LINE_NUMBER,
       t.ARD_SEQUENCE,
       t.ARD_OPERATION_CODE,
       t.ARD_BIN,
       t.ARD_GANTT,
       t.ARD_OPERATION_DETAILS,
       t.ARD_MAIL_GROUP_NAME
FROM   DB2ADMIN.SCDC_AUTO_RUN_DEFINITION t
FETCH FIRST 100 ROWS ONLY;
```
