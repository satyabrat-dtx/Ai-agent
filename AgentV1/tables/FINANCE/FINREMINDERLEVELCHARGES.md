# DB2ADMIN.FINREMINDERLEVELCHARGES

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `FINRMDLVLTMPFINRMDTMPCMYCODE`, `FINRMDLVLTMPFINRMDTMPCODE`, `FINREMINDERLEVELTEMPLATECODE`, `CURRENCYCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 101769

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINRMDLVLTMPFINRMDTMPCMYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINRMDLVLTMPFINRMDTMPCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FINREMINDERLEVELTEMPLATECODE` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CURRENCYCODE` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 4 | `CHARGE` | DECIMAL(15,2) |  |  |  |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINREMINDERLEVELTEMPLATE_CHARGES` | `FINRMDLVLTMPFINRMDTMPCMYCODE`, `FINRMDLVLTMPFINRMDTMPCODE`, `FINREMINDERLEVELTEMPLATECODE` | [`FINREMINDERLEVELTEMPLATE`](../FINANCE/FINREMINDERLEVELTEMPLATE.md) | `FINREMINDERTEMPLATECOMPANYCODE`, `FINREMINDERTEMPLATECODE`, `CODE` | RESTRICT | `FINREMINDERLEVELCHARGES.FINRMDLVLTMPFINRMDTMPCMYCODE = FINREMINDERLEVELTEMPLATE.FINREMINDERTEMPLATECOMPANYCODE AND FINREMINDERLEVELCHARGES.FINRMDLVLTMPFINRMDTMPCODE = FINREMINDERLEVELTEMPLATE.FINREMINDERTEMPLATECODE AND FINREMINDERLEVELCHARGES.FINREMINDERLEVELTEMPLATECODE = FINREMINDERLEVELTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINREMINDERLEVELCHARGESUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINRMDLVLTMPFINRMDTMPCMYCODE,
       t.FINRMDLVLTMPFINRMDTMPCODE,
       t.FINREMINDERLEVELTEMPLATECODE,
       t.CURRENCYCODE,
       t.CHARGE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.FINREMINDERLEVELCHARGES t
FETCH FIRST 100 ROWS ONLY;
```
