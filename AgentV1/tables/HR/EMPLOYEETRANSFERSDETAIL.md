# DB2ADMIN.EMPLOYEETRANSFERSDETAIL

- **Module**: `HR` (high confidence — table name starts with 'EMPLOYEE')
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `EMPLOYEETRANSFERSFROMCMYCODE`, `EMPLOYEETRANSFERSEMPLOYEEIDCOD`, `EMPLOYEETRANSFERSNEWEMPCODE`, `EMPLOYEETRANSFERSTOCOMPANYCODE`, `EFFECTIVEFROM`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 166090

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EMPLOYEETRANSFERSFROMCMYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EMPLOYEETRANSFERSEMPLOYEEIDCOD` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EMPLOYEETRANSFERSNEWEMPCODE` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `EMPLOYEETRANSFERSTOCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `INCOMETAXINFO` | INTEGER | NOT NULL |  |  |  |
| 5 | `LEAVEDATA` | INTEGER | NOT NULL |  |  |  |
| 6 | `PFNO` | INTEGER | NOT NULL |  |  |  |
| 7 | `ESINO` | INTEGER | NOT NULL |  |  |  |
| 8 | `LOANDATA` | INTEGER | NOT NULL |  |  |  |
| 9 | `SUPERANNAUTIONDATA` | INTEGER | NOT NULL |  |  |  |
| 10 | `REIMBURSEMENTDATA` | INTEGER | NOT NULL |  |  |  |
| 11 | `PAYTEMPLATEDATA` | INTEGER | NOT NULL |  |  |  |
| 12 | `ATTENDANCEDATA` | INTEGER | NOT NULL |  |  |  |
| 13 | `EFFECTIVEFROM` | DATE | NOT NULL | PK | primary_key |  |
| 14 | `NEWJOININGDATE` | DATE |  |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EMPLOYEETRANSFERS_LINE` | `EMPLOYEETRANSFERSFROMCMYCODE`, `EMPLOYEETRANSFERSEMPLOYEEIDCOD`, `EMPLOYEETRANSFERSNEWEMPCODE`, `EMPLOYEETRANSFERSTOCOMPANYCODE` | [`EMPLOYEETRANSFERS`](../HR/EMPLOYEETRANSFERS.md) | `FROMCOMPANYCODE`, `EMPLOYEEIDCODE`, `NEWEMPCODE`, `TOCOMPANYCODE` | RESTRICT | `EMPLOYEETRANSFERSDETAIL.EMPLOYEETRANSFERSFROMCMYCODE = EMPLOYEETRANSFERS.FROMCOMPANYCODE AND EMPLOYEETRANSFERSDETAIL.EMPLOYEETRANSFERSEMPLOYEEIDCOD = EMPLOYEETRANSFERS.EMPLOYEEIDCODE AND EMPLOYEETRANSFERSDETAIL.EMPLOYEETRANSFERSNEWEMPCODE = EMPLOYEETRANSFERS.NEWEMPCODE AND EMPLOYEETRANSFERSDETAIL.EMPLOYEETRANSFERSTOCOMPANYCODE = EMPLOYEETRANSFERS.TOCOMPANYCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EMPLOYEETRANSFERSDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EMPLOYEETRANSFERSFROMCMYCODE,
       t.EMPLOYEETRANSFERSEMPLOYEEIDCOD,
       t.EMPLOYEETRANSFERSNEWEMPCODE,
       t.EMPLOYEETRANSFERSTOCOMPANYCODE,
       t.INCOMETAXINFO,
       t.LEAVEDATA,
       t.PFNO,
       t.ESINO,
       t.LOANDATA,
       t.SUPERANNAUTIONDATA,
       t.REIMBURSEMENTDATA,
       t.PAYTEMPLATEDATA
FROM   DB2ADMIN.EMPLOYEETRANSFERSDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
