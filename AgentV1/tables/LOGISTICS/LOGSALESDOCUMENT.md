# DB2ADMIN.LOGSALESDOCUMENT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 165
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 53934

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
| 6 | `PROVISIONALCOUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 7 | `PROVISIONALCODE` | CHAR(15) | NOT NULL |  |  |  |
| 8 | `PROVISIONALDOCUMENTDATE` | DATE | NOT NULL |  |  |  |
| 9 | `DEFINITIVECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 10 | `DEFINITIVECODE` | CHAR(15) |  |  |  |  |
| 11 | `DEFINITIVEDOCUMENTDATE` | DATE |  |  |  |  |
| 12 | `GOODSISSUEDATE` | DATE |  |  |  |  |
| 13 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 14 | `ORDERPARTNERBRANDCODE` | CHAR(8) |  |  |  |  |
| 15 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 16 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
| 17 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 18 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 19 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 20 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 21 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 22 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 23 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 24 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 25 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 26 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 27 | `REGISTERTAXCODE` | CHAR(3) |  |  |  |  |
| 28 | `GROUPSHIPPINGSONINVOICE` | INTEGER | NOT NULL |  |  |  |
| 29 | `CONSIGNMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 30 | `CONSIGNMENTWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 31 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 32 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 33 | `TERMSOFDELIVERYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 34 | `TERMSOFSHIPPINGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 35 | `APPEARANCEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 36 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 37 | `AREACODE` | CHAR(3) |  |  |  |  |
| 38 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 39 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 40 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 41 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 42 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 43 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 44 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 45 | `TRUCKDRIVERCODE` | CHAR(3) |  |  |  |  |
| 46 | `NUMBERPLATE` | VARCHAR(80) |  |  |  |  |
| 47 | `TRANSPORTSTARTDATE` | DATE |  |  |  |  |
| 48 | `TRANSPORTSTARTTIME` | TIME |  |  |  |  |
| 49 | `NUMBERPARCEL` | DECIMAL(5,0) |  |  |  |  |
| 50 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 51 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 52 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 53 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 54 | `VOLUMEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 55 | `VOLUME` | DECIMAL(15,5) |  |  |  |  |
| 56 | `UPDATEWAREHOUSEAVAILABILITY` | SMALLINT | NOT NULL |  |  |  |
| 57 | `STOCKTRANSACTIONCREATED` | SMALLINT | NOT NULL |  |  |  |
| 58 | `TRACKINGNUMBER` | CHAR(25) |  |  |  |  |
| 59 | `FNCORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 60 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 61 | `MARKETCODE` | CHAR(10) |  |  |  |  |
| 62 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 63 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 64 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 65 | `PRICEANDDISCOUNTDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 66 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 67 | `PAYMENTSTARTINGDATE` | DATE |  |  |  |  |
| 68 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 69 | `DISCOUNTCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 70 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 71 | `ONDOCUMENTTOTALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 72 | `ONINVOICETOTALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 73 | `PAYMENTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 74 | `PAYMENTCUSTOMERUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 75 | `PAYMENTCUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 76 | `MINAMOUNTACHIEVEMENTINVOICE` | SMALLINT | NOT NULL |  |  |  |
| 77 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 78 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 79 | `BANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 80 | `ORDERPARTNERBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 81 | `COMPANYBANKCODE` | CHAR(15) |  |  |  |  |
| 82 | `COMPANYBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 83 | `COMPANYBANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 84 | `COMPANYBANKIDIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 85 | `ACCTRNTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 86 | `COMMISSIONTRANSACTIONCREATED` | SMALLINT | NOT NULL |  |  |  |
| 87 | `INVOICEEVOLUTIONTYPE` | CHAR(2) |  |  |  |  |
| 88 | `COMMISSIONDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 89 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 90 | `COMMISSIONLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 91 | `AGENTCREATIONTYPE1` | CHAR(1) | NOT NULL |  |  |  |
| 92 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 93 | `COMMISSIONLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 94 | `AGENTCREATIONTYPE2` | CHAR(1) | NOT NULL |  |  |  |
| 95 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 96 | `COMMISSIONLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 97 | `AGENTCREATIONTYPE3` | CHAR(1) | NOT NULL |  |  |  |
| 98 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 99 | `COMMISSIONLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 100 | `AGENTCREATIONTYPE4` | CHAR(1) | NOT NULL |  |  |  |
| 101 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 102 | `COMMISSIONLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 103 | `AGENTCREATIONTYPE5` | CHAR(1) | NOT NULL |  |  |  |
| 104 | `CURRENTSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 105 | `LINESUSPENDED` | SMALLINT | NOT NULL |  |  |  |
| 106 | `PROGRESSSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 107 | `PRINTEDDOCUMENT` | SMALLINT | NOT NULL |  |  |  |
| 108 | `ORDERSOURCE` | CHAR(2) | NOT NULL |  |  |  |
| 109 | `PREVIOUSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 110 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 111 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 112 | `SALESORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 113 | `SALESORDERCODE` | CHAR(15) |  |  |  |  |
| 114 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 115 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 116 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 117 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 118 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 119 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 120 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 121 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 122 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 123 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 124 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 125 | `PROVISIONALCOUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 126 | `DEFINITIVECOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 127 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 128 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 129 | `CONSIGNMENTWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 130 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 131 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 132 | `TRANSPORTREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 133 | `AREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 134 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 135 | `TRUCKDRIVERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 136 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 137 | `PREVIOUSCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 138 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 139 | `COMPANYBANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 140 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 141 | `DECLARATIONCODE1` | DECIMAL(23,0) |  |  |  |  |
| 142 | `DECLARATIONYEAR1` | DECIMAL(4,0) |  |  |  |  |
| 143 | `DECLARATIONVALUE1` | DECIMAL(18,5) |  |  |  |  |
| 144 | `DECLARATIONCODE2` | DECIMAL(23,0) |  |  |  |  |
| 145 | `DECLARATIONYEAR2` | DECIMAL(4,0) |  |  |  |  |
| 146 | `DECLARATIONVALUE2` | DECIMAL(18,5) |  |  |  |  |
| 147 | `KEEPENTRYEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 148 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 149 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 150 | `LEGALDOCUMENTTYPECODE` | CHAR(4) |  |  |  |  |
| 151 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 152 | `RFORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 153 | `PAYMENTSTATUS` | INTEGER | NOT NULL |  |  |  |
| 154 | `PAIDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 155 | `INVOICELIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 156 | `PAYMENTLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 157 | `INVOICELIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 158 | `PAYMENTLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 159 | `INVOICELIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 160 | `PAYMENTLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 161 | `INVOICELIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 162 | `PAYMENTLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 163 | `INVOICELIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 164 | `PAYMENTLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGSALESDOCUMENT.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGSALESDOCUMENTBLOCKS`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGSALESDOCUMENTCHARGE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGSALESDOCUMENTCOMMISSION`.`FATHERID` → this table's `ABSUNIQUEID` (medium confidence)
- child `LOGSALESDOCUMENTDISCOUNT`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)
- child `LOGSALESDOCUMENTLINE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COMPANYCODE,
       t.TEMPLATECODE,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE,
       t.PROVISIONALCOUNTERCODE,
       t.PROVISIONALCODE,
       t.PROVISIONALDOCUMENTDATE,
       t.DEFINITIVECOUNTERCODE,
       t.DEFINITIVECODE,
       t.DEFINITIVEDOCUMENTDATE
FROM   DB2ADMIN.LOGSALESDOCUMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
