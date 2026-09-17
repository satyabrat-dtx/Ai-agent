# DB2ADMIN.SCDA_CALENDAR

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `CA_IDENTIFIER`, `CA_CAL`, `CA_CAL_DATE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 183786

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CA_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `CA_CAL` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `CA_CAL_DATE` | TIMESTAMP | NOT NULL | PK | primary_key |  |
| 3 | `CA_PROG_WRK_HR` | DECIMAL(9,2) |  |  |  |  |
| 4 | `CA_SH1_START` | SMALLINT |  |  |  |  |
| 5 | `CA_SH1_END` | SMALLINT |  |  |  |  |
| 6 | `CA_SH2_START` | SMALLINT |  |  |  |  |
| 7 | `CA_SH2_END` | SMALLINT |  |  |  |  |
| 8 | `CA_SH3_START` | SMALLINT |  |  |  |  |
| 9 | `CA_SH3_END` | SMALLINT |  |  |  |  |
| 10 | `CA_SH4_START` | SMALLINT |  |  |  |  |
| 11 | `CA_SH4_END` | SMALLINT |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CA_IDENTIFIER,
       t.CA_CAL,
       t.CA_CAL_DATE,
       t.CA_PROG_WRK_HR,
       t.CA_SH1_START,
       t.CA_SH1_END,
       t.CA_SH2_START,
       t.CA_SH2_END,
       t.CA_SH3_START,
       t.CA_SH3_END,
       t.CA_SH4_START,
       t.CA_SH4_END
FROM   DB2ADMIN.SCDA_CALENDAR t
FETCH FIRST 100 ROWS ONLY;
```
