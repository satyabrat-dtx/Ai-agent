# DB2ADMIN.REIMBURSEMENTCLAIMBILLS

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `RECLDETAILRECLAIMCOMPANYCODE`, `RECLDETAILRECLAIMCODE`, `RECLAIMDETAILGROUPCODE`, `RECLDETAILRETYPECODE`, `SRNO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 168317

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RECLDETAILRECLAIMCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `RECLDETAILRECLAIMCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `RECLAIMDETAILGROUPCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `RECLDETAILRETYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SRNO` | BIGINT | NOT NULL | PK | primary_key |  |
| 5 | `BILLNUMBER` | CHAR(20) | NOT NULL |  |  |  |
| 6 | `BILLSDATE` | DATE | NOT NULL |  |  |  |
| 7 | `BILLAMOUNT` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `REIMBURSEMENTCLAIMDETAIL_BILLDETAIL` | `RECLDETAILRECLAIMCOMPANYCODE`, `RECLDETAILRECLAIMCODE`, `RECLAIMDETAILGROUPCODE`, `RECLDETAILRETYPECODE` | [`REIMBURSEMENTCLAIMDETAIL`](../HR/REIMBURSEMENTCLAIMDETAIL.md) | `REIMBURSEMENTCLAIMCOMPANYCODE`, `REIMBURSEMENTCLAIMCODE`, `GROUPCODE`, `REIMBURSEMENTTYPECODE` | RESTRICT | `REIMBURSEMENTCLAIMBILLS.RECLDETAILRECLAIMCOMPANYCODE = REIMBURSEMENTCLAIMDETAIL.REIMBURSEMENTCLAIMCOMPANYCODE AND REIMBURSEMENTCLAIMBILLS.RECLDETAILRECLAIMCODE = REIMBURSEMENTCLAIMDETAIL.REIMBURSEMENTCLAIMCODE AND REIMBURSEMENTCLAIMBILLS.RECLAIMDETAILGROUPCODE = REIMBURSEMENTCLAIMDETAIL.GROUPCODE AND REIMBURSEMENTCLAIMBILLS.RECLDETAILRETYPECODE = REIMBURSEMENTCLAIMDETAIL.REIMBURSEMENTTYPECODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `REIMBURSEMENTCLAIMBILLSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.RECLDETAILRECLAIMCOMPANYCODE,
       t.RECLDETAILRECLAIMCODE,
       t.RECLAIMDETAILGROUPCODE,
       t.RECLDETAILRETYPECODE,
       t.SRNO,
       t.BILLNUMBER,
       t.BILLSDATE,
       t.BILLAMOUNT,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.REIMBURSEMENTCLAIMBILLS t
FETCH FIRST 100 ROWS ONLY;
```
