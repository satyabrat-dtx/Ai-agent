# DB2ADMIN.ROUTINGSTEPCOMMENT

- **Module**: `PRODUCTION` (high confidence — table name starts with 'ROUTING')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `ROUTINGSTEPROUTINGCOMPANYCODE`, `ROUTINGSTEPROUTINGNUMBERID`, `ROUTINGSTEPSEQUENCE`, `ROUTINGSTEPSUBSEQUENCE`, `ORIGIN`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 5150

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ROUTINGSTEPROUTINGCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ROUTINGSTEPROUTINGNUMBERID` | DECIMAL(11,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ROUTINGSTEPSEQUENCE` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ROUTINGSTEPSUBSEQUENCE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 5 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 7 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 8 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ROUTINGSTEP_COMMENTS` | `ROUTINGSTEPROUTINGCOMPANYCODE`, `ROUTINGSTEPROUTINGNUMBERID`, `ROUTINGSTEPSEQUENCE`, `ROUTINGSTEPSUBSEQUENCE` | [`ROUTINGSTEP`](../PRODUCTION/ROUTINGSTEP.md) | `ROUTINGCOMPANYCODE`, `ROUTINGNUMBERID`, `SEQUENCE`, `SUBSEQUENCE` | RESTRICT | `ROUTINGSTEPCOMMENT.ROUTINGSTEPROUTINGCOMPANYCODE = ROUTINGSTEP.ROUTINGCOMPANYCODE AND ROUTINGSTEPCOMMENT.ROUTINGSTEPROUTINGNUMBERID = ROUTINGSTEP.ROUTINGNUMBERID AND ROUTINGSTEPCOMMENT.ROUTINGSTEPSEQUENCE = ROUTINGSTEP.SEQUENCE AND ROUTINGSTEPCOMMENT.ROUTINGSTEPSUBSEQUENCE = ROUTINGSTEP.SUBSEQUENCE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ROUTINGSTEPCOMMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ROUTINGSTEPROUTINGCOMPANYCODE,
       t.ROUTINGSTEPROUTINGNUMBERID,
       t.ROUTINGSTEPSEQUENCE,
       t.ROUTINGSTEPSUBSEQUENCE,
       t.REPORTTYPE,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE,
       t.CANCELED,
       t.ABSUNIQUEID,
       t.CREATIONDATETIME
FROM   DB2ADMIN.ROUTINGSTEPCOMMENT t
FETCH FIRST 100 ROWS ONLY;
```
