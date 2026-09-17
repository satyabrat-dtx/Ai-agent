# DB2ADMIN.LCTYPE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `CODE`
- **FK degree**: referenced by 5 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 129348

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 8 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 9 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 5

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `LCTYPE_LCTYPE` | [`LCAMENDMENTPUR`](../FINANCE/LCAMENDMENTPUR.md) | `LCTYPECODE` | `LCAMENDMENTPUR.LCTYPECODE = LCTYPE.CODE` |
| `LCTYPE_LCTYPE` | [`LCAMENDMENT`](../PURCHASING/LCAMENDMENT.md) | `LCTYPECODE` | `LCAMENDMENT.LCTYPECODE = LCTYPE.CODE` |
| `LCTYPE_LCTYPE` | [`LCDETAIL`](../PURCHASING/LCDETAIL.md) | `LCTYPECODE` | `LCDETAIL.LCTYPECODE = LCTYPE.CODE` |
| `LCTYPE_LCTYPE` | [`LCDETAILPUR`](../FINANCE/LCDETAILPUR.md) | `LCTYPECODE` | `LCDETAILPUR.LCTYPECODE = LCTYPE.CODE` |
| `LCTYPE_LCTYPE` | [`LCAPPLICATION`](../COSTING/LCAPPLICATION.md) | `LCTYPECODE` | `LCAPPLICATION.LCTYPECODE = LCTYPE.CODE` |

## Indexes

- `LCTYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.LCTYPE t
FETCH FIRST 100 ROWS ONLY;
```
