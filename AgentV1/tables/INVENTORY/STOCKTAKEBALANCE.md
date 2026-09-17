# DB2ADMIN.STOCKTAKEBALANCE

- **Module**: `INVENTORY` (high confidence — table name starts with 'STOCK')
- **Roles**: `business_data`
- **Columns**: 67
- **Primary key**: `COMPANYCODE`, `STOCKTAKEIDENTIFIER`, `STOCKTAKEIDENTIFIERLINE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 18946

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `STOCKTAKEIDENTIFIER` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `STOCKTAKEIDENTIFIERLINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `STOCKTAKECRITERIA` | CHAR(2) | NOT NULL |  |  |  |
| 4 | `STOCKTAKEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 5 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 7 | `DECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 8 | `DECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 9 | `DECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 10 | `DECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 11 | `DECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 12 | `DECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 13 | `DECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 14 | `DECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 15 | `DECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 16 | `DECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 17 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  | FK | foreign_key |  |
| 18 | `WHSLOCATIONWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 19 | `WAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 20 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 21 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 22 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 23 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 24 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 25 | `ELEMENTSSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 26 | `ELEMENTSCODE` | CHAR(15) |  |  |  |  |
| 27 | `LISTNUMBER` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 28 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 29 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 30 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 31 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 32 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 33 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 34 | `STOCKTYPECODE` | CHAR(3) |  |  |  |  |
| 35 | `BASEPRIMARYUNITCODE` | CHAR(3) |  | FK | foreign_key |  |
| 36 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 37 | `BASESECONDARYUNITCODE` | CHAR(3) |  | FK | foreign_key |  |
| 38 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 39 | `PACKAGINGCODE` | CHAR(3) |  |  |  |  |
| 40 | `PACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 41 | `BASEPRIMARYQUANTITYVERIFIED` | DECIMAL(15,5) |  |  |  |  |
| 42 | `BASESECONDARYQUANTITYVERIFIED` | DECIMAL(15,5) |  |  |  |  |
| 43 | `PACKAGINGQUANTITYVERIFIED` | DECIMAL(15,5) |  |  |  |  |
| 44 | `VERIFIEDLINE` | SMALLINT | NOT NULL |  |  |  |
| 45 | `ADJUSTMENTTRANSACTIONMADE` | CHAR(2) |  |  |  |  |
| 46 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 47 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 48 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 49 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 50 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 51 | `PHYSICALWAREHOUSECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 52 | `MANUALLYINSERTED` | SMALLINT | NOT NULL |  |  |  |
| 53 | `STBALANCESTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 54 | `VERIFIEDLOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 55 | `VERIFIEDPHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 56 | `VERIFIEDWHSLOCWHSZONECODE` | CHAR(3) |  |  |  |  |
| 57 | `VERIFIEDWAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 58 | `VERIFIEDCONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 59 | `VERIFIEDCONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 60 | `VERIFIEDCONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 61 | `ADJUSTMENTTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 62 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 63 | `TRANSFERMISSINGQUANTITY` | SMALLINT | NOT NULL |  |  |  |
| 64 | `ISNEWELEMENT` | SMALLINT | NOT NULL |  |  |  |
| 65 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 66 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `STOCKTAKEBALANCE.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `STOCKTAKEBALANCE.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND STOCKTAKEBALANCE.ITEMTYPECODE = ITEMTYPE.CODE` |
| `PHYSICALWAREHOUSE_PHYSICALWAREHOUSE` | `PHYSICALWAREHOUSECOMPANYCODE`, `PHYSICALWAREHOUSECODE` | [`PHYSICALWAREHOUSE`](../CORE_MASTER/PHYSICALWAREHOUSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `STOCKTAKEBALANCE.PHYSICALWAREHOUSECOMPANYCODE = PHYSICALWAREHOUSE.COMPANYCODE AND STOCKTAKEBALANCE.PHYSICALWAREHOUSECODE = PHYSICALWAREHOUSE.CODE` |
| `UNITOFMEASURE_BASEPRIMARYUNIT` | `BASEPRIMARYUNITCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `STOCKTAKEBALANCE.BASEPRIMARYUNITCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_BASESECONDARYUNIT` | `BASESECONDARYUNITCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `STOCKTAKEBALANCE.BASESECONDARYUNITCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `STOCKTAKEBALANCEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.STOCKTAKEIDENTIFIER,
       t.STOCKTAKEIDENTIFIERLINE,
       t.STOCKTAKECRITERIA,
       t.STOCKTAKEPRIORITY,
       t.ITEMTYPECODE,
       t.LOGICALWAREHOUSECODE,
       t.DECOSUBCODE01,
       t.DECOSUBCODE02,
       t.DECOSUBCODE03,
       t.DECOSUBCODE04,
       t.DECOSUBCODE05
FROM   DB2ADMIN.STOCKTAKEBALANCE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
