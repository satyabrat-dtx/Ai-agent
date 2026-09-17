# DB2ADMIN.TNASELECTIVEDATA

- **Module**: `TNA` (low confidence — table name starts with 'TNA')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `UNIQUEID`, `COMPANY`, `HEADERCODE`, `ACTIVITYCODE`, `SEQNO`, `LINE`, `CODE`, `ACTIVITYACTIONSPOLICYCODE`, `DESCRIPTION`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 195901

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `COMPANY` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `HEADERCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ACTIVITYCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SEQNO` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `LINE` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `CODE` | CHAR(50) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 7 | `ACTIVITYACTIONSPOLICYCODE` | CHAR(30) | NOT NULL | PK | primary_key |  |
| 8 | `DESCRIPTION` | CHAR(100) | NOT NULL | PK | primary_key description |  |
| 9 | `CHECKDATA` | SMALLINT | NOT NULL |  |  |  |
| 10 | `LOCKDATA` | SMALLINT | NOT NULL |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `ISATTRIBUTE` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `TNAACTIVITYACTIONS_SELECTIVEPOLICYDATA` | `UNIQUEID`, `COMPANY`, `HEADERCODE`, `ACTIVITYCODE`, `SEQNO`, `LINE` | [`TNAACTIVITYACTIONS`](../TNA/TNAACTIVITYACTIONS.md) | `UNIQUEID`, `COMPANY`, `TNAHEADERCODE`, `ACTIVITYCODE`, `SEQNO`, `LINENUMBER` | RESTRICT | `TNASELECTIVEDATA.UNIQUEID = TNAACTIVITYACTIONS.UNIQUEID AND TNASELECTIVEDATA.COMPANY = TNAACTIVITYACTIONS.COMPANY AND TNASELECTIVEDATA.HEADERCODE = TNAACTIVITYACTIONS.TNAHEADERCODE AND TNASELECTIVEDATA.ACTIVITYCODE = TNAACTIVITYACTIONS.ACTIVITYCODE AND TNASELECTIVEDATA.SEQNO = TNAACTIVITYACTIONS.SEQNO AND TNASELECTIVEDATA.LINE = TNAACTIVITYACTIONS.LINENUMBER` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TNASELECTIVEDATAUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.UNIQUEID,
       t.COMPANY,
       t.HEADERCODE,
       t.ACTIVITYCODE,
       t.SEQNO,
       t.LINE,
       t.CODE,
       t.ACTIVITYACTIONSPOLICYCODE,
       t.DESCRIPTION,
       t.CHECKDATA,
       t.LOCKDATA,
       t.ABSUNIQUEID
FROM   DB2ADMIN.TNASELECTIVEDATA t
FETCH FIRST 100 ROWS ONLY;
```
