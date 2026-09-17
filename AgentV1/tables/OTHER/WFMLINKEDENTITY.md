# DB2ADMIN.WFMLINKEDENTITY

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `REFERENCEDENTITY`, `REFERENCEDENTITYPK`, `WFMPROCESSID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 96926

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `REFERENCEDENTITY` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `REFERENCEDENTITYPK` | CHAR(140) | NOT NULL | PK | primary_key |  |
| 2 | `WFMPROCESSID` | CHAR(120) | NOT NULL | PK | primary_key |  |
| 3 | `WFMPROCESSKEY` | CHAR(50) | NOT NULL |  |  |  |
| 4 | `UIXMLPATH` | VARCHAR(50) |  |  |  |  |
| 5 | `UIXMLNAME` | VARCHAR(54) |  |  |  |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `PISTATUS` | INTEGER | NOT NULL |  |  |  |
| 12 | `GROUPFAMILY` | CHAR(15) |  |  |  |  |
| 13 | `REFERENCEDENTITYGROUP` | CHAR(140) |  |  |  |  |
| 14 | `REASONCODE` | CHAR(50) |  | FK | foreign_key |  |
| 15 | `REMARK` | CLOB(2000000) |  |  |  |  |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `WFMSTATUSREASON_REASON` | `REASONCODE` | [`WFMSTATUSREASON`](../OTHER/WFMSTATUSREASON.md) | `CODE` | RESTRICT | `WFMLINKEDENTITY.REASONCODE = WFMSTATUSREASON.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WFMLINKEDENTITYUID` (ABSUNIQUEID)
- `WFMLINKEDENTITYIDX1` (WFMPROCESSID)
- `WFMLINKEDENTITYIDX2` (REFERENCEDENTITY, REFERENCEDENTITYPK)
- `WFMLINKEDENTITYCDT` (CREATIONDATETIME, PISTATUS)

## Starter query

```sql
SELECT t.REFERENCEDENTITY,
       t.REFERENCEDENTITYPK,
       t.WFMPROCESSID,
       t.WFMPROCESSKEY,
       t.UIXMLPATH,
       t.UIXMLNAME,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.PISTATUS
FROM   DB2ADMIN.WFMLINKEDENTITY t
FETCH FIRST 100 ROWS ONLY;
```
