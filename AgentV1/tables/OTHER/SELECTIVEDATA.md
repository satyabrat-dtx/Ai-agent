# DB2ADMIN.SELECTIVEDATA

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `COMPANY`, `HEADERCODE`, `SEQNO`, `LINE`, `CODE`, `ACTIVITYACTIONSPOLICYCODE`, `DESCRIPTION`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 195108

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANY` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `HEADERCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SEQNO` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINE` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CODE` | CHAR(50) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `ACTIVITYACTIONSPOLICYCODE` | CHAR(30) | NOT NULL | PK | primary_key |  |
| 6 | `DESCRIPTION` | CHAR(100) | NOT NULL | PK | primary_key description |  |
| 7 | `CHECKDATA` | SMALLINT | NOT NULL |  |  |  |
| 8 | `LOCKDATA` | SMALLINT | NOT NULL |  |  |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 10 | `ISATTRIBUTE` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACTIVITYACTIONS_SELECTIVEPOLICYDATA` | `COMPANY`, `HEADERCODE`, `SEQNO`, `LINE` | [`ACTIVITYACTIONS`](../OTHER/ACTIVITYACTIONS.md) | `TNADETAILTNAHEADERCOMPANYCODE`, `TNADETAILTNAHEADERCODE`, `TNADETAILSEQNO`, `LINENUMBER` | RESTRICT | `SELECTIVEDATA.COMPANY = ACTIVITYACTIONS.TNADETAILTNAHEADERCOMPANYCODE AND SELECTIVEDATA.HEADERCODE = ACTIVITYACTIONS.TNADETAILTNAHEADERCODE AND SELECTIVEDATA.SEQNO = ACTIVITYACTIONS.TNADETAILSEQNO AND SELECTIVEDATA.LINE = ACTIVITYACTIONS.LINENUMBER` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SELECTIVEDATAUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANY,
       t.HEADERCODE,
       t.SEQNO,
       t.LINE,
       t.CODE,
       t.ACTIVITYACTIONSPOLICYCODE,
       t.DESCRIPTION,
       t.CHECKDATA,
       t.LOCKDATA,
       t.ABSUNIQUEID,
       t.ISATTRIBUTE
FROM   DB2ADMIN.SELECTIVEDATA t
FETCH FIRST 100 ROWS ONLY;
```
