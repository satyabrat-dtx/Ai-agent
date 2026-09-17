# DB2ADMIN.SCDA_WRKCNTRANDOPERATTRIBUTES

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 34
- **Primary key**: `IDENTIFIER`, `WORKCENTERCODE`, `OPERATIONCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 184965

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `WORKCENTERCODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `OPERATIONCODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `CODE` | VARCHAR(20) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `STANDARDSTEPQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 6 | `STANDARDSTEPQTYUOMCODE` | VARCHAR(3) |  |  |  |  |
| 7 | `STEPEFFICIENCYAPPLY` | CHAR(1) |  |  |  |  |
| 8 | `STEPEFFICIENCY` | DECIMAL(5,2) |  |  |  |  |
| 9 | `TIMETYPE1CODE` | VARCHAR(3) |  |  |  |  |
| 10 | `TIME1` | DECIMAL(10,5) |  |  |  |  |
| 11 | `TIMEUNIT1` | VARCHAR(2) |  |  |  |  |
| 12 | `TIMEREFQTY1` | DECIMAL(15,5) |  |  |  |  |
| 13 | `TIMEREFUOM1CODE` | VARCHAR(3) |  |  |  |  |
| 14 | `TIMETYPE2CODE` | VARCHAR(3) |  |  |  |  |
| 15 | `TIME2` | DECIMAL(10,5) |  |  |  |  |
| 16 | `TIMEUNIT2` | VARCHAR(2) |  |  |  |  |
| 17 | `TIMEREFQTY2` | DECIMAL(15,5) |  |  |  |  |
| 18 | `TIMEREFUOM2CODE` | VARCHAR(3) |  |  |  |  |
| 19 | `TIMETYPE3CODE` | VARCHAR(3) |  |  |  |  |
| 20 | `TIME3` | DECIMAL(10,5) |  |  |  |  |
| 21 | `TIMEUNIT3` | VARCHAR(2) |  |  |  |  |
| 22 | `TIMEREFQTY3` | DECIMAL(15,5) |  |  |  |  |
| 23 | `TIMEREFUOM3CODE` | VARCHAR(3) |  |  |  |  |
| 24 | `TIMETYPE4CODE` | VARCHAR(3) |  |  |  |  |
| 25 | `TIME4` | DECIMAL(10,5) |  |  |  |  |
| 26 | `TIMEUNIT4` | VARCHAR(2) |  |  |  |  |
| 27 | `TIMEREFQTY4` | DECIMAL(15,5) |  |  |  |  |
| 28 | `TIMEREFUOM4CODE` | VARCHAR(3) |  |  |  |  |
| 29 | `TIMETYPE5CODE` | VARCHAR(3) |  |  |  |  |
| 30 | `TIME5` | DECIMAL(10,5) |  |  |  |  |
| 31 | `TIMEUNIT5` | VARCHAR(2) |  |  |  |  |
| 32 | `TIMEREFQTY5` | DECIMAL(15,5) |  |  |  |  |
| 33 | `TIMEREFUOM5CODE` | VARCHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IDENTIFIER,
       t.WORKCENTERCODE,
       t.OPERATIONCODE,
       t.CODE,
       t.SHORTDESCRIPTION,
       t.STANDARDSTEPQUANTITY,
       t.STANDARDSTEPQTYUOMCODE,
       t.STEPEFFICIENCYAPPLY,
       t.STEPEFFICIENCY,
       t.TIMETYPE1CODE,
       t.TIME1,
       t.TIMEUNIT1
FROM   DB2ADMIN.SCDA_WRKCNTRANDOPERATTRIBUTES t
FETCH FIRST 100 ROWS ONLY;
```
