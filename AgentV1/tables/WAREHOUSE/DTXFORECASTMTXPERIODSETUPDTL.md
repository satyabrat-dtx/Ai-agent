# DB2ADMIN.DTXFORECASTMTXPERIODSETUPDTL

- **Module**: `WAREHOUSE` (low confidence — FK neighbourhood: 1 of 1 related tables are WAREHOUSE)
- **Roles**: `business_data`
- **Columns**: 45
- **Primary key**: `FORECASTMTXSETUPCOMPANYCODE`, `FORECASTMTXSETUPCODE`, `ITEMTYPECODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 204576

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FORECASTMTXSETUPCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FORECASTMTXSETUPCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `MATRIXSEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 3 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 4 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `SUBCODE01CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 6 | `SUBCODE02CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 7 | `SUBCODE03CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 8 | `SUBCODE04CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 9 | `SUBCODE05CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `SUBCODE06CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 11 | `SUBCODE07CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `SUBCODE08CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 13 | `SUBCODE09CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 14 | `SUBCODE10CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 15 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 16 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 17 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 18 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 19 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 20 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 21 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 22 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 23 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 24 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 25 | `NOTMANAGEDSUBCODE01` | CHAR(20) |  |  |  |  |
| 26 | `NOTMANAGEDSUBCODE02` | CHAR(10) |  |  |  |  |
| 27 | `NOTMANAGEDSUBCODE03` | CHAR(10) |  |  |  |  |
| 28 | `NOTMANAGEDSUBCODE04` | CHAR(10) |  |  |  |  |
| 29 | `NOTMANAGEDSUBCODE05` | CHAR(10) |  |  |  |  |
| 30 | `NOTMANAGEDSUBCODE06` | CHAR(10) |  |  |  |  |
| 31 | `NOTMANAGEDSUBCODE07` | CHAR(10) |  |  |  |  |
| 32 | `NOTMANAGEDSUBCODE08` | CHAR(10) |  |  |  |  |
| 33 | `NOTMANAGEDSUBCODE09` | CHAR(10) |  |  |  |  |
| 34 | `NOTMANAGEDSUBCODE10` | CHAR(10) |  |  |  |  |
| 35 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 36 | `WAREHOUSECODE` | CHAR(8) |  | FK | foreign_key |  |
| 37 | `LINENUMBER` | INTEGER | NOT NULL |  |  |  |
| 38 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 39 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 40 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 41 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 42 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 43 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 44 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `DTXFORECASTMTXPERIODSETUP_DETAIL` | `FORECASTMTXSETUPCOMPANYCODE`, `FORECASTMTXSETUPCODE` | [`DTXFORECASTMTXPERIODSETUP`](../SALES/DTXFORECASTMTXPERIODSETUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DTXFORECASTMTXPERIODSETUPDTL.FORECASTMTXSETUPCOMPANYCODE = DTXFORECASTMTXPERIODSETUP.COMPANYCODE AND DTXFORECASTMTXPERIODSETUPDTL.FORECASTMTXSETUPCODE = DTXFORECASTMTXPERIODSETUP.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DTXFORECASTMTXPERIODSETUPDTL.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND DTXFORECASTMTXPERIODSETUPDTL.ITEMTYPECODE = ITEMTYPE.CODE` |
| `LOGICALWAREHOUSE_WAREHOUSE` | `WAREHOUSECOMPANYCODE`, `WAREHOUSECODE` | [`LOGICALWAREHOUSE`](../WAREHOUSE/LOGICALWAREHOUSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DTXFORECASTMTXPERIODSETUPDTL.WAREHOUSECOMPANYCODE = LOGICALWAREHOUSE.COMPANYCODE AND DTXFORECASTMTXPERIODSETUPDTL.WAREHOUSECODE = LOGICALWAREHOUSE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DTXFRCMTXPERIODSETUPDTLUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FORECASTMTXSETUPCOMPANYCODE,
       t.FORECASTMTXSETUPCODE,
       t.MATRIXSEQUENCE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01CONTROLLED,
       t.SUBCODE02CONTROLLED,
       t.SUBCODE03CONTROLLED,
       t.SUBCODE04CONTROLLED,
       t.SUBCODE05CONTROLLED,
       t.SUBCODE06CONTROLLED,
       t.SUBCODE07CONTROLLED
FROM   DB2ADMIN.DTXFORECASTMTXPERIODSETUPDTL t
FETCH FIRST 100 ROWS ONLY;
```
