# DB2ADMIN.ACTIVITYACTIONS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `TNADETAILTNAHEADERCOMPANYCODE`, `TNADETAILTNAHEADERCODE`, `TNADETAILSEQNO`, `LINENUMBER`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 191043

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TNADETAILTNAHEADERCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TNADETAILSEQNO` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINENUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 4 | `ISVALIDATION` | SMALLINT | NOT NULL |  |  |  |
| 5 | `ACTIVITYACTIONSPOLICYCODE` | CHAR(20) |  |  |  |  |
| 6 | `ENTITYENTITY` | CHAR(50) |  |  |  |  |
| 7 | `DECISIONTABLEGROUPFAMILY` | CHAR(15) |  | FK | foreign_key |  |
| 8 | `DECISIONTABLEREFERENCEDENTITY` | CHAR(50) |  | FK | foreign_key |  |
| 9 | `DECISIONTABLEDTRPKTOKEN` | CHAR(15) |  | FK | foreign_key |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 17 | `TNADETAILTNAHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 18 | `TNAFROMCOPY` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSDTRENTITY_DECISIONTABLE` | `DECISIONTABLEGROUPFAMILY`, `DECISIONTABLEREFERENCEDENTITY`, `DECISIONTABLEDTRPKTOKEN` | [`ABSDTRENTITY`](../PLATFORM/ABSDTRENTITY.md) | `GROUPFAMILY`, `REFERENCEDENTITY`, `DTRPKTOKEN` | RESTRICT | `ACTIVITYACTIONS.DECISIONTABLEGROUPFAMILY = ABSDTRENTITY.GROUPFAMILY AND ACTIVITYACTIONS.DECISIONTABLEREFERENCEDENTITY = ABSDTRENTITY.REFERENCEDENTITY AND ACTIVITYACTIONS.DECISIONTABLEDTRPKTOKEN = ABSDTRENTITY.DTRPKTOKEN` |
| `TNADETAIL_ACTIONS` | `TNADETAILTNAHEADERCOMPANYCODE`, `TNADETAILTNAHEADERCODE`, `TNADETAILSEQNO` | [`TNADETAIL`](../TNA/TNADETAIL.md) | `TNAHEADERCOMPANYCODE`, `TNAHEADERCODE`, `SEQNO` | RESTRICT | `ACTIVITYACTIONS.TNADETAILTNAHEADERCOMPANYCODE = TNADETAIL.TNAHEADERCOMPANYCODE AND ACTIVITYACTIONS.TNADETAILTNAHEADERCODE = TNADETAIL.TNAHEADERCODE AND ACTIVITYACTIONS.TNADETAILSEQNO = TNADETAIL.SEQNO` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ACTIVITYACTIONS_SELECTIVEPOLICYDATA` | [`SELECTIVEDATA`](../OTHER/SELECTIVEDATA.md) | `COMPANY`, `HEADERCODE`, `SEQNO`, `LINE` | `SELECTIVEDATA.COMPANY = ACTIVITYACTIONS.TNADETAILTNAHEADERCOMPANYCODE AND SELECTIVEDATA.HEADERCODE = ACTIVITYACTIONS.TNADETAILTNAHEADERCODE AND SELECTIVEDATA.SEQNO = ACTIVITYACTIONS.TNADETAILSEQNO AND SELECTIVEDATA.LINE = ACTIVITYACTIONS.LINENUMBER` |

## Indexes

- `ACTIVITYACTIONSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TNADETAILTNAHEADERCODE,
       t.TNADETAILSEQNO,
       t.LINENUMBER,
       t.SEQUENCE,
       t.ISVALIDATION,
       t.ACTIVITYACTIONSPOLICYCODE,
       t.ENTITYENTITY,
       t.DECISIONTABLEGROUPFAMILY,
       t.DECISIONTABLEREFERENCEDENTITY,
       t.DECISIONTABLEDTRPKTOKEN,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.ACTIVITYACTIONS t
FETCH FIRST 100 ROWS ONLY;
```
