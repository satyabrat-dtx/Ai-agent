# DB2ADMIN.PREVIOUSACTIVITIES

- **Module**: `TNA` (low confidence — FK neighbourhood: 1 of 1 related tables are TNA)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `TNADETAILTNAHEADERCOMPANYCODE`, `TNADETAILTNAHEADERCODE`, `TNADETAILSEQNO`, `SEQUENCETNAHEADERCODE`, `SEQUENCESEQNO`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 191581

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TNADETAILTNAHEADERCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TNADETAILSEQNO` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SEQUENCETNAHEADERCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SEQUENCESEQNO` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 8 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 9 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `TNADETAILTNAHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `TNADETAIL_PREVIOUSACTIVITIES` | `TNADETAILTNAHEADERCOMPANYCODE`, `TNADETAILTNAHEADERCODE`, `TNADETAILSEQNO` | [`TNADETAIL`](../TNA/TNADETAIL.md) | `TNAHEADERCOMPANYCODE`, `TNAHEADERCODE`, `SEQNO` | RESTRICT | `PREVIOUSACTIVITIES.TNADETAILTNAHEADERCOMPANYCODE = TNADETAIL.TNAHEADERCOMPANYCODE AND PREVIOUSACTIVITIES.TNADETAILTNAHEADERCODE = TNADETAIL.TNAHEADERCODE AND PREVIOUSACTIVITIES.TNADETAILSEQNO = TNADETAIL.SEQNO` |
| `TNADETAIL_SEQUENCE` | `TNADETAILTNAHEADERCOMPANYCODE`, `SEQUENCETNAHEADERCODE`, `SEQUENCESEQNO` | [`TNADETAIL`](../TNA/TNADETAIL.md) | `TNAHEADERCOMPANYCODE`, `TNAHEADERCODE`, `SEQNO` | RESTRICT | `PREVIOUSACTIVITIES.TNADETAILTNAHEADERCOMPANYCODE = TNADETAIL.TNAHEADERCOMPANYCODE AND PREVIOUSACTIVITIES.SEQUENCETNAHEADERCODE = TNADETAIL.TNAHEADERCODE AND PREVIOUSACTIVITIES.SEQUENCESEQNO = TNADETAIL.SEQNO` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PREVIOUSACTIVITIESUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TNADETAILTNAHEADERCODE,
       t.TNADETAILSEQNO,
       t.SEQUENCETNAHEADERCODE,
       t.SEQUENCESEQNO,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID,
       t.TNADETAILTNAHEADERCOMPANYCODE
FROM   DB2ADMIN.PREVIOUSACTIVITIES t
FETCH FIRST 100 ROWS ONLY;
```
