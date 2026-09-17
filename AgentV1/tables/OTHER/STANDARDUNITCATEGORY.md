# DB2ADMIN.STANDARDUNITCATEGORY

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `TYPE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 26057

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TYPE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 1 | `BASEUNITOFMEASURECODE` | CHAR(3) |  | FK | foreign_key |  |
| 2 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 3 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 4 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 5 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 7 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 8 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `UNITOFMEASURE_BASEUNITOFMEASURE` | `BASEUNITOFMEASURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `STANDARDUNITCATEGORY.BASEUNITOFMEASURECODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `STANDARDUNITCATEGORY_STANDARDUNITCATEGORYCONVERTION` | [`STDUNITCATEGORYCONVERSION`](../OTHER/STDUNITCATEGORYCONVERSION.md) | `STANDARDUNITCATEGORYTYPE` | `STDUNITCATEGORYCONVERSION.STANDARDUNITCATEGORYTYPE = STANDARDUNITCATEGORY.TYPE` |

## Indexes

- `STANDARDUNITCATEGORYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TYPE,
       t.BASEUNITOFMEASURECODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.STANDARDUNITCATEGORY t
FETCH FIRST 100 ROWS ONLY;
```
