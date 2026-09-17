# DB2ADMIN.APPROVALREQUESTDLTDLVPOINT

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `COMPANY`, `CODE`, `VERSION`, `LINE`, `ADDRESSUNIQUEID`, `ADDRESSCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 211088

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANY` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `VERSION` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINE` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `ADDRESSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 5 | `ADDRESSCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `APPROVALREQUESTDETAIL_APPROVALREQUESTDELIVERYPOINT` | `COMPANY`, `CODE`, `VERSION`, `LINE` | [`APPROVALREQUESTDETAIL`](../PLATFORM/APPROVALREQUESTDETAIL.md) | `APPROVALREQUESTCOMPANYCODE`, `APPROVALREQUESTREQUESTCODE`, `APPROVALREQUESTVERSION`, `LINENR` | RESTRICT | `APPROVALREQUESTDLTDLVPOINT.COMPANY = APPROVALREQUESTDETAIL.APPROVALREQUESTCOMPANYCODE AND APPROVALREQUESTDLTDLVPOINT.CODE = APPROVALREQUESTDETAIL.APPROVALREQUESTREQUESTCODE AND APPROVALREQUESTDLTDLVPOINT.VERSION = APPROVALREQUESTDETAIL.APPROVALREQUESTVERSION AND APPROVALREQUESTDLTDLVPOINT.LINE = APPROVALREQUESTDETAIL.LINENR` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `APPROVALREQUESTDLTDLVPOINTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANY,
       t.CODE,
       t.VERSION,
       t.LINE,
       t.ADDRESSUNIQUEID,
       t.ADDRESSCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.APPROVALREQUESTDLTDLVPOINT t
FETCH FIRST 100 ROWS ONLY;
```
