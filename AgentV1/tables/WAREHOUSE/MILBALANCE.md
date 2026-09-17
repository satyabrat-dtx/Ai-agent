# DB2ADMIN.MILBALANCE

- **Module**: `WAREHOUSE` (low confidence — FK neighbourhood: 1 of 1 related tables are WAREHOUSE)
- **Roles**: `business_data`
- **Columns**: 30
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`, `LOGICALWAREHOUSECODE`, `DECOSUBCODE01`, `DECOSUBCODE02`, `DECOSUBCODE03`, `DECOSUBCODE04`, `DECOSUBCODE05`, `DECOSUBCODE06`, `DECOSUBCODE07`, `DECOSUBCODE08`, `DECOSUBCODE09`, `DECOSUBCODE10`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 33473

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LOGICALWAREHOUSECODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `DECOSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `DECOSUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 5 | `DECOSUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 6 | `DECOSUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 7 | `DECOSUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 8 | `DECOSUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 9 | `DECOSUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 10 | `DECOSUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 11 | `DECOSUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 12 | `DECOSUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 13 | `UNITOFMEASURECODE` | CHAR(3) | NOT NULL |  |  |  |
| 14 | `BALANCEQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 15 | `AVAILABILITY01` | DECIMAL(15,5) |  |  |  |  |
| 16 | `AVAILABILITY02` | DECIMAL(15,5) |  |  |  |  |
| 17 | `DATEIMMEDIATE` | DATE |  |  |  |  |
| 18 | `DATE01` | DATE |  |  |  |  |
| 19 | `DATE02` | DATE |  |  |  |  |
| 20 | `ORDERONBALANCE` | DECIMAL(15,5) |  |  |  |  |
| 21 | `ORDERONAVAIL01` | DECIMAL(15,5) |  |  |  |  |
| 22 | `ORDERONAVAIL02` | DECIMAL(15,5) |  |  |  |  |
| 23 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 24 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 25 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 26 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 27 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 28 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `MILBALANCE.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MILBALANCE.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND MILBALANCE.ITEMTYPECODE = ITEMTYPE.CODE` |
| `LOGICALWAREHOUSE_LOGICALWAREHOUSE` | `LOGICALWAREHOUSECOMPANYCODE`, `LOGICALWAREHOUSECODE` | [`LOGICALWAREHOUSE`](../WAREHOUSE/LOGICALWAREHOUSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MILBALANCE.LOGICALWAREHOUSECOMPANYCODE = LOGICALWAREHOUSE.COMPANYCODE AND MILBALANCE.LOGICALWAREHOUSECODE = LOGICALWAREHOUSE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `MILBALANCEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECODE,
       t.LOGICALWAREHOUSECODE,
       t.DECOSUBCODE01,
       t.DECOSUBCODE02,
       t.DECOSUBCODE03,
       t.DECOSUBCODE04,
       t.DECOSUBCODE05,
       t.DECOSUBCODE06,
       t.DECOSUBCODE07,
       t.DECOSUBCODE08,
       t.DECOSUBCODE09
FROM   DB2ADMIN.MILBALANCE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
