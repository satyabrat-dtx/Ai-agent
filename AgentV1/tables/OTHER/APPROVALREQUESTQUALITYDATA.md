# DB2ADMIN.APPROVALREQUESTQUALITYDATA

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `APPROVALREQUESTCOMPANYCODE`, `APPROVALREQUESTREQUESTCODE`, `APPROVALREQUESTVERSION`, `QUALITYDATACODE`, `QUALITYDATASUBGROUPCODE`, `QUALITYDATANUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 213354

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `APPROVALREQUESTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `APPROVALREQUESTREQUESTCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `APPROVALREQUESTVERSION` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `QUALITYDATACODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `QUALITYDATASUBGROUPCODE` | CHAR(5) | NOT NULL | PK | primary_key |  |
| 5 | `QUALITYDATANUMBERID` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `APPROVALREQUEST_APPROVALREQUESTQUALITYDATA` | `APPROVALREQUESTCOMPANYCODE`, `APPROVALREQUESTREQUESTCODE`, `APPROVALREQUESTVERSION` | [`APPROVALREQUEST`](../CORE_MASTER/APPROVALREQUEST.md) | `COMPANYCODE`, `REQUESTCODE`, `VERSION` | RESTRICT | `APPROVALREQUESTQUALITYDATA.APPROVALREQUESTCOMPANYCODE = APPROVALREQUEST.COMPANYCODE AND APPROVALREQUESTQUALITYDATA.APPROVALREQUESTREQUESTCODE = APPROVALREQUEST.REQUESTCODE AND APPROVALREQUESTQUALITYDATA.APPROVALREQUESTVERSION = APPROVALREQUEST.VERSION` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `APPROVALREQUESTQUALITYDATAUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.APPROVALREQUESTCOMPANYCODE,
       t.APPROVALREQUESTREQUESTCODE,
       t.APPROVALREQUESTVERSION,
       t.QUALITYDATACODE,
       t.QUALITYDATASUBGROUPCODE,
       t.QUALITYDATANUMBERID,
       t.ABSUNIQUEID
FROM   DB2ADMIN.APPROVALREQUESTQUALITYDATA t
FETCH FIRST 100 ROWS ONLY;
```
