# DB2ADMIN.EXTOPERATIONPRICEDETAIL

- **Module**: `SUBCONTRACTING` (medium confidence — table name starts with 'EXTOPERATION')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `EXTOPPRCEXTOPPRCLISTCMYCODE`, `EXTOPPRICEEXTOPPRICELISTCODE`, `EXTOPPRICELINEID`, `NUMBERLINEID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 30237

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EXTOPPRCEXTOPPRCLISTCMYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EXTOPPRICEEXTOPPRICELISTCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EXTOPPRICELINEID` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `NUMBERLINEID` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 4 | `BREAKDOWNLIMIT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 5 | `PRICETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 6 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 7 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EXTOPPRICE_PRICEDETAIL` | `EXTOPPRCEXTOPPRCLISTCMYCODE`, `EXTOPPRICEEXTOPPRICELISTCODE`, `EXTOPPRICELINEID` | [`EXTOPPRICE`](../SUBCONTRACTING/EXTOPPRICE.md) | `EXTOPPRICELISTCOMPANYCODE`, `EXTOPPRICELISTCODE`, `LINEID` | RESTRICT | `EXTOPERATIONPRICEDETAIL.EXTOPPRCEXTOPPRCLISTCMYCODE = EXTOPPRICE.EXTOPPRICELISTCOMPANYCODE AND EXTOPERATIONPRICEDETAIL.EXTOPPRICEEXTOPPRICELISTCODE = EXTOPPRICE.EXTOPPRICELISTCODE AND EXTOPERATIONPRICEDETAIL.EXTOPPRICELINEID = EXTOPPRICE.LINEID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EXTOPERATIONPRICEDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EXTOPPRCEXTOPPRCLISTCMYCODE,
       t.EXTOPPRICEEXTOPPRICELISTCODE,
       t.EXTOPPRICELINEID,
       t.NUMBERLINEID,
       t.BREAKDOWNLIMIT,
       t.PRICETYPE,
       t.PRICE,
       t.PRICEINCLUDINGTAX,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.EXTOPERATIONPRICEDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
