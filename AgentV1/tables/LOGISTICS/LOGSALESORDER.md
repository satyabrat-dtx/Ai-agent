# DB2ADMIN.LOGSALESORDER

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 137
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 54725

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 1 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 4 | `ORDERTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 5 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 6 | `INTERCOMPANYREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 7 | `INTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `COUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 9 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 10 | `ORDERDATE` | DATE | NOT NULL |  |  |  |
| 11 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 12 | `ORDERPARTNERBRANDCODE` | CHAR(8) |  |  |  |  |
| 13 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 14 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
| 15 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 16 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 17 | `DESCRIPTION` | VARCHAR(200) |  |  | description |  |
| 18 | `INITIALDATE` | DATE |  |  |  |  |
| 19 | `FINALDATE` | DATE |  |  |  |  |
| 20 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 21 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 22 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 23 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 24 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 25 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 26 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 27 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 28 | `MARKETCODE` | CHAR(10) |  |  |  |  |
| 29 | `GROUPORDERSONSHIPPING` | INTEGER | NOT NULL |  |  |  |
| 30 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 31 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 32 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 33 | `AREACODE` | CHAR(3) |  |  |  |  |
| 34 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 35 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 36 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 37 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 38 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 39 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 40 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 41 | `REQUIREDDUEDATE` | DATE |  |  |  |  |
| 42 | `CONFIRMEDDUEDATE` | DATE |  |  |  |  |
| 43 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 44 | `RELEASEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 45 | `FNCORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 46 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 47 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 48 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 49 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 50 | `PRICEANDDISCOUNTDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 51 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 52 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 53 | `DISCOUNTCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 54 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 55 | `ONORDERTOTALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 56 | `PAYMENTCUSTOMERUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 57 | `PAYMENTCUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 58 | `MINAMOUNTACHIEVEMENTINVOICE` | SMALLINT | NOT NULL |  |  |  |
| 59 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 60 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 61 | `BANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 62 | `ORDERPARTNERBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 63 | `COMPANYBANKCODE` | CHAR(15) |  |  |  |  |
| 64 | `COMPANYBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 65 | `COMPANYBANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 66 | `COMPANYBANKIDIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 67 | `THIRDPARTYBILLING` | SMALLINT | NOT NULL |  |  |  |
| 68 | `COMMISSIONDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 69 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 70 | `COMMISSIONLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 71 | `AGENTCREATIONTYPE1` | CHAR(1) | NOT NULL |  |  |  |
| 72 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 73 | `COMMISSIONLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 74 | `AGENTCREATIONTYPE2` | CHAR(1) | NOT NULL |  |  |  |
| 75 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 76 | `COMMISSIONLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 77 | `AGENTCREATIONTYPE3` | CHAR(1) | NOT NULL |  |  |  |
| 78 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 79 | `COMMISSIONLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 80 | `AGENTCREATIONTYPE4` | CHAR(1) | NOT NULL |  |  |  |
| 81 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 82 | `COMMISSIONLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 83 | `AGENTCREATIONTYPE5` | CHAR(1) | NOT NULL |  |  |  |
| 84 | `CURRENTSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 85 | `LINESUSPENDED` | SMALLINT | NOT NULL |  |  |  |
| 86 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 87 | `ORDERSOURCE` | CHAR(2) | NOT NULL |  |  |  |
| 88 | `PREVIOUSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 89 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 90 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 91 | `PRINTEDCONFIRMATION` | SMALLINT | NOT NULL |  |  |  |
| 92 | `LINESUNMATCHEDWITHBOX` | SMALLINT | NOT NULL |  |  |  |
| 93 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 94 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 95 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 96 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 97 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 98 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 99 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 100 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 101 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 102 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 103 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 104 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 105 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 106 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 107 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 108 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 109 | `TRANSPORTREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 110 | `AREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 111 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 112 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 113 | `PREVIOUSCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 114 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 115 | `COMPANYBANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 116 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 117 | `PURORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 118 | `PURORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 119 | `KEEPENTRYEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 120 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 121 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 122 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 123 | `RFORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 124 | `WFMORDERSTATUS` | INTEGER | NOT NULL |  |  |  |
| 125 | `PURORDERCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 126 | `PLANNINGGROUPINGCODE` | CHAR(3) |  |  |  |  |
| 127 | `INVOICELIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 128 | `PAYMENTLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 129 | `INVOICELIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 130 | `PAYMENTLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 131 | `INVOICELIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 132 | `PAYMENTLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 133 | `INVOICELIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 134 | `PAYMENTLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 135 | `INVOICELIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 136 | `PAYMENTLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGSALESORDER.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGSALESORDERASSORTMENT`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGSALESORDERBLOCKS`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGSALESORDERCHARGE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGSALESORDERCOMMISSION`.`FATHERID` → this table's `ABSUNIQUEID` (medium confidence)
- child `LOGSALESORDERDELIVERY`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGSALESORDERDISCOUNT`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGSALESORDERLINE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGSALESORDERTEMPLATE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COMPANYCODE,
       t.TEMPLATECODE,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE,
       t.INTERCOMPANYREQUIRED,
       t.INTERCOMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.ORDERDATE,
       t.ORDPRNCUSTOMERSUPPLIERCODE
FROM   DB2ADMIN.LOGSALESORDER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
