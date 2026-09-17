# DB2ADMIN.SHIPMENTARTICLEDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `SHIPMENTARTICLECOMPANYCODE`, `SHIPMENTARTICLECODE`, `PGSCHEMETYPECODE`, `PGPRODUCTGROUPCODE`, `PGDEPBSRNO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 124907

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SHIPMENTARTICLECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SHIPMENTARTICLECODE` | CHAR(5) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PGSCHEMETYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `PGPRODUCTGROUPCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `PGDEPBSRNO` | CHAR(20) | NOT NULL | PK | primary_key |  |
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
| `SHIPMENTARTICLE_SHIPMENTARTICLEDETAIL` | `SHIPMENTARTICLECOMPANYCODE`, `SHIPMENTARTICLECODE` | [`SHIPMENTARTICLE`](../OTHER/SHIPMENTARTICLE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SHIPMENTARTICLEDETAIL.SHIPMENTARTICLECOMPANYCODE = SHIPMENTARTICLE.COMPANYCODE AND SHIPMENTARTICLEDETAIL.SHIPMENTARTICLECODE = SHIPMENTARTICLE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SHIPMENTARTICLEDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SHIPMENTARTICLECOMPANYCODE,
       t.SHIPMENTARTICLECODE,
       t.PGSCHEMETYPECODE,
       t.PGPRODUCTGROUPCODE,
       t.PGDEPBSRNO,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.SHIPMENTARTICLEDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
