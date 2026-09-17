# DB2ADMIN.EMAILRECIPIENT

- **Module**: `TNA` (low confidence — FK neighbourhood: 1 of 1 related tables are TNA)
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `TNADETAILTNAHEADERCOMPANYCODE`, `TNADETAILTNAHEADERCODE`, `TNADETAILSEQNO`, `MAILADDRESS`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 194823

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TNADETAILTNAHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TNADETAILTNAHEADERCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `TNADETAILSEQNO` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `MAILADDRESS` | CHAR(120) | NOT NULL | PK | primary_key |  |
| 4 | `MAILADDRESSCHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `TNADETAIL_EMAILRECIPIENT` | `TNADETAILTNAHEADERCOMPANYCODE`, `TNADETAILTNAHEADERCODE`, `TNADETAILSEQNO` | [`TNADETAIL`](../TNA/TNADETAIL.md) | `TNAHEADERCOMPANYCODE`, `TNAHEADERCODE`, `SEQNO` | RESTRICT | `EMAILRECIPIENT.TNADETAILTNAHEADERCOMPANYCODE = TNADETAIL.TNAHEADERCOMPANYCODE AND EMAILRECIPIENT.TNADETAILTNAHEADERCODE = TNADETAIL.TNAHEADERCODE AND EMAILRECIPIENT.TNADETAILSEQNO = TNADETAIL.SEQNO` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EMAILRECIPIENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TNADETAILTNAHEADERCOMPANYCODE,
       t.TNADETAILTNAHEADERCODE,
       t.TNADETAILSEQNO,
       t.MAILADDRESS,
       t.MAILADDRESSCHOOSE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.EMAILRECIPIENT t
FETCH FIRST 100 ROWS ONLY;
```
