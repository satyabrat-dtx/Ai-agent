# DB2ADMIN.TNAEMAILRECIPIENT

- **Module**: `TNA` (low confidence — table name starts with 'TNA')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `UNIQUEID`, `COMPANY`, `TNAHEADERCODE`, `ACTIVITYCODE`, `SEQNO`, `MAILADDRESS`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 195698

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `COMPANY` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `TNAHEADERCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ACTIVITYCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SEQNO` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `MAILADDRESS` | CHAR(120) | NOT NULL | PK | primary_key |  |
| 6 | `MAILADDRESSCHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `TNAACTIVITYDETAIL_EMAILRECIPIENT` | `UNIQUEID`, `COMPANY`, `TNAHEADERCODE`, `ACTIVITYCODE`, `SEQNO` | [`TNAACTIVITYDETAIL`](../TNA/TNAACTIVITYDETAIL.md) | `TNAACTIVITYUNIQUEID`, `TNAACTIVITYTNAHDRCOMPANYCODE`, `TNAACTIVITYTNAHEADERCODE`, `ACTIVITYCODECODE`, `SEQNO` | RESTRICT | `TNAEMAILRECIPIENT.UNIQUEID = TNAACTIVITYDETAIL.TNAACTIVITYUNIQUEID AND TNAEMAILRECIPIENT.COMPANY = TNAACTIVITYDETAIL.TNAACTIVITYTNAHDRCOMPANYCODE AND TNAEMAILRECIPIENT.TNAHEADERCODE = TNAACTIVITYDETAIL.TNAACTIVITYTNAHEADERCODE AND TNAEMAILRECIPIENT.ACTIVITYCODE = TNAACTIVITYDETAIL.ACTIVITYCODECODE AND TNAEMAILRECIPIENT.SEQNO = TNAACTIVITYDETAIL.SEQNO` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TNAEMAILRECIPIENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.UNIQUEID,
       t.COMPANY,
       t.TNAHEADERCODE,
       t.ACTIVITYCODE,
       t.SEQNO,
       t.MAILADDRESS,
       t.MAILADDRESSCHOOSE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.TNAEMAILRECIPIENT t
FETCH FIRST 100 ROWS ONLY;
```
