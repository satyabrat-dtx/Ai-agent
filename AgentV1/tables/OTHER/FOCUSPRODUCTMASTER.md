# DB2ADMIN.FOCUSPRODUCTMASTER

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `TARIFFCODE`, `FOCUSSCHEME`, `EFFECTIVEFROMDATE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 139243

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TARIFFCODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FOCUSSCHEME` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 2 | `RATE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 3 | `EFFECTIVEFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 4 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `TARIFF_TARIFF` | `TARIFFCODE` | [`TARIFF`](../CORE_MASTER/TARIFF.md) | `CODE` | RESTRICT | `FOCUSPRODUCTMASTER.TARIFFCODE = TARIFF.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FOCUSPRODUCTMASTER_DETAIL` | [`FOCUSPRODUCTMASTERDETAIL`](../OTHER/FOCUSPRODUCTMASTERDETAIL.md) | `FOCUSPRODUCTMASTERTARIFFCODE`, `FOCUSPRODUCTMASTERFOCUSSCHEME`, `FOCUSPRDMEFFECTIVEFROMDATE` | `FOCUSPRODUCTMASTERDETAIL.FOCUSPRODUCTMASTERTARIFFCODE = FOCUSPRODUCTMASTER.TARIFFCODE AND FOCUSPRODUCTMASTERDETAIL.FOCUSPRODUCTMASTERFOCUSSCHEME = FOCUSPRODUCTMASTER.FOCUSSCHEME AND FOCUSPRODUCTMASTERDETAIL.FOCUSPRDMEFFECTIVEFROMDATE = FOCUSPRODUCTMASTER.EFFECTIVEFROMDATE` |

## Indexes

- `FOCUSPRODUCTMASTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TARIFFCODE,
       t.FOCUSSCHEME,
       t.RATE,
       t.EFFECTIVEFROMDATE,
       t.EFFECTIVETODATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.FOCUSPRODUCTMASTER t
FETCH FIRST 100 ROWS ONLY;
```
