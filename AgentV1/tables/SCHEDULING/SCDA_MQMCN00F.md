# DB2ADMIN.SCDA_MQMCN00F

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `IDENTIFIER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 184601

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `KSRSTT` | CHAR(1) | NOT NULL |  |  |  |
| 2 | `KSRSTR` | TIMESTAMP | NOT NULL |  |  |  |
| 3 | `KSREND` | TIMESTAMP | NOT NULL |  |  |  |
| 4 | `KCLSTT` | CHAR(1) | NOT NULL |  |  |  |
| 5 | `KCLSTR` | TIMESTAMP | NOT NULL |  |  |  |
| 6 | `KCLEND` | TIMESTAMP | NOT NULL |  |  |  |
| 7 | `KCLOPR` | CHAR(1) | NOT NULL |  |  |  |
| 8 | `KCLUPL` | CHAR(1) | NOT NULL |  |  |  |
| 9 | `KSRUPD` | CHAR(1) | NOT NULL |  |  |  |
| 10 | `KUPDAT` | TIMESTAMP | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IDENTIFIER,
       t.KSRSTT,
       t.KSRSTR,
       t.KSREND,
       t.KCLSTT,
       t.KCLSTR,
       t.KCLEND,
       t.KCLOPR,
       t.KCLUPL,
       t.KSRUPD,
       t.KUPDAT
FROM   DB2ADMIN.SCDA_MQMCN00F t
FETCH FIRST 100 ROWS ONLY;
```
