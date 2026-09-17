# DB2ADMIN.BUNDLELAYINFO

- **Module**: `PRODUCTION` (low confidence — FK neighbourhood: 1 of 1 related tables are PRODUCTION)
- **Roles**: `business_data`
- **Columns**: 42
- **Primary key**: `COMPANYCODE`, `PRODORDERCODE`, `LAYNO`, `ELEMENTNO`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 126483

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PRODORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LAYNO` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `MARKERCODE` | CHAR(15) |  |  |  |  |
| 4 | `CUTNO` | CHAR(9) |  |  |  |  |
| 5 | `LAYLENGTH` | DECIMAL(7,2) |  |  |  |  |
| 6 | `TRANSACTIONNO` | CHAR(15) |  |  |  |  |
| 7 | `ELEMENTNO` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 8 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 9 | `CALCULATEDLAYERS` | INTEGER | NOT NULL |  |  |  |
| 10 | `LOTNO` | CHAR(10) |  |  |  |  |
| 11 | `LAYSTATUS` | CHAR(1) |  |  |  |  |
| 12 | `WIDTHRANGE` | DECIMAL(5,2) |  |  |  |  |
| 13 | `GSMRANGE` | DECIMAL(5,2) |  |  |  |  |
| 14 | `PRIORITYNO` | INTEGER | NOT NULL |  |  |  |
| 15 | `ACTUALLAYER` | INTEGER | NOT NULL |  |  |  |
| 16 | `DEFECTQTY` | DECIMAL(15,5) |  |  |  |  |
| 17 | `EXCESSQTY` | DECIMAL(15,5) |  |  |  |  |
| 18 | `SHORTQTY` | DECIMAL(15,5) |  |  |  |  |
| 19 | `OVERLAPPINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 20 | `OTHERDEFECTSQTY` | DECIMAL(15,5) |  |  |  |  |
| 21 | `USABLEFABRIC` | DECIMAL(15,5) |  |  |  |  |
| 22 | `ENDBIT` | DECIMAL(7,2) |  |  |  |  |
| 23 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 24 | `DSTSUBCODE01` | CHAR(20) |  |  |  |  |
| 25 | `DSTSUBCODE02` | CHAR(10) |  |  |  |  |
| 26 | `DSTSUBCODE03` | CHAR(10) |  |  |  |  |
| 27 | `DSTSUBCODE04` | CHAR(10) |  |  |  |  |
| 28 | `DSTSUBCODE05` | CHAR(10) |  |  |  |  |
| 29 | `DSTSUBCODE06` | CHAR(10) |  |  |  |  |
| 30 | `DSTSUBCODE07` | CHAR(10) |  |  |  |  |
| 31 | `DSTSUBCODE08` | CHAR(10) |  |  |  |  |
| 32 | `DSTSUBCODE09` | CHAR(10) |  |  |  |  |
| 33 | `DSTSUBCODE10` | CHAR(10) |  |  |  |  |
| 34 | `DEFECTCUTS` | DECIMAL(15,5) |  |  |  |  |
| 35 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 36 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 37 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 38 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 39 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 40 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 41 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `BUNDLELAYINFO.COMPANYCODE = COMPANY.CODE` |
| `PRODUCTIONORDER_PRODORDER` | `COMPANYCODE`, `PRODORDERCODE` | [`PRODUCTIONORDER`](../PRODUCTION/PRODUCTIONORDER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BUNDLELAYINFO.COMPANYCODE = PRODUCTIONORDER.COMPANYCODE AND BUNDLELAYINFO.PRODORDERCODE = PRODUCTIONORDER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BUNDLELAYINFOUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PRODORDERCODE,
       t.LAYNO,
       t.MARKERCODE,
       t.CUTNO,
       t.LAYLENGTH,
       t.TRANSACTIONNO,
       t.ELEMENTNO,
       t.BASEPRIMARYUOMCODE,
       t.CALCULATEDLAYERS,
       t.LOTNO,
       t.LAYSTATUS
FROM   DB2ADMIN.BUNDLELAYINFO t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
