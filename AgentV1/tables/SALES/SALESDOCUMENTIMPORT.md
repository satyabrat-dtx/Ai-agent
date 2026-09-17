# DB2ADMIN.SALESDOCUMENTIMPORT

- **Module**: `SALES` (high confidence — table name starts with 'SALESDOCUMENT')
- **Roles**: `business_data`
- **Columns**: 115
- **Primary key**: `COMPANYCODE`, `IMPORTPROVISIONALCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 40196

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 1 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `IMPORTOPERATION` | INTEGER | NOT NULL |  |  |  |
| 4 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 5 | `IMPORTPROVISIONALCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 6 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 7 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 8 | `PROVISIONALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 9 | `PROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 10 | `PROVISIONALDOCUMENTDATE` | DATE |  |  |  |  |
| 11 | `DEFDOCIDREQ` | SMALLINT | NOT NULL |  |  |  |
| 12 | `DEFINITIVECODE` | CHAR(15) |  |  |  |  |
| 13 | `DEFINITIVEDOCUMENTDATE` | DATE |  |  |  |  |
| 14 | `GOODSISSUEDATE` | DATE |  |  |  |  |
| 15 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 16 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 17 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
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
| 28 | `CONSIGNMENTTYPE` | CHAR(2) |  |  |  |  |
| 29 | `CONSIGNMENTWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 30 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 31 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 32 | `TERMSOFDELIVERYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 33 | `TERMSOFSHIPPINGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 34 | `APPEARANCEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 35 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 36 | `AREACODE` | CHAR(3) |  |  |  |  |
| 37 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 38 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 39 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 40 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 41 | `THIRDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 42 | `THIRDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 43 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 44 | `TRUCKDRIVERCODE` | CHAR(3) |  |  |  |  |
| 45 | `NUMBERPLATE` | VARCHAR(80) |  |  |  |  |
| 46 | `TRANSPORTSTARTDATE` | DATE |  |  |  |  |
| 47 | `TRANSPORTSTARTTIME` | TIME |  |  |  |  |
| 48 | `NUMBERPARCEL` | DECIMAL(5,0) |  |  |  |  |
| 49 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 50 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 51 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 52 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 53 | `VOLUMEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 54 | `VOLUME` | DECIMAL(15,5) |  |  |  |  |
| 55 | `FNCORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 56 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 57 | `MARKETCODE` | CHAR(10) |  |  |  |  |
| 58 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 59 | `ENTRYEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 60 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 61 | `PRICEANDDISCOUNTDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 62 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 63 | `PAYMENTSTARTINGDATE` | DATE |  |  |  |  |
| 64 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 65 | `DISCOUNTCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 66 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 67 | `PAYMENTCUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 68 | `ORDERPARTNERBANKIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 69 | `COMMISSIONDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 70 | `AGENT1CODE` | CHAR(3) |  |  |  |  |
| 71 | `COMMISSIONLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 72 | `AGENT2CODE` | CHAR(3) |  |  |  |  |
| 73 | `COMMISSIONLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 74 | `AGENT3CODE` | CHAR(3) |  |  |  |  |
| 75 | `COMMISSIONLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 76 | `AGENT4CODE` | CHAR(3) |  |  |  |  |
| 77 | `COMMISSIONLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 78 | `AGENT5CODE` | CHAR(3) |  |  |  |  |
| 79 | `COMMISSIONLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 80 | `CURRENTSTATUS` | CHAR(2) |  |  |  |  |
| 81 | `ADUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 82 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 83 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 84 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 85 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 86 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 87 | `PREVIOUSTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 88 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 89 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 90 | `PROVISIONALCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 91 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 92 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 93 | `CONSIGNMENTWHSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 94 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 95 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 96 | `TRANSPORTREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 97 | `AREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 98 | `WAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 99 | `TRUCKDRIVERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 100 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 101 | `PREVIOUSCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 102 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 103 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 104 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 105 | `PAYMENTLIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 106 | `INVOICELIQUIDATIONTYPE1` | INTEGER | NOT NULL |  |  |  |
| 107 | `PAYMENTLIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 108 | `INVOICELIQUIDATIONTYPE2` | INTEGER | NOT NULL |  |  |  |
| 109 | `PAYMENTLIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 110 | `INVOICELIQUIDATIONTYPE3` | INTEGER | NOT NULL |  |  |  |
| 111 | `PAYMENTLIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 112 | `INVOICELIQUIDATIONTYPE4` | INTEGER | NOT NULL |  |  |  |
| 113 | `PAYMENTLIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |
| 114 | `INVOICELIQUIDATIONTYPE5` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESDOCUMENTIMPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.IMPORTSTATUS,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.IMPORTOPERATION,
       t.COMPANYCODE,
       t.IMPORTPROVISIONALCODE,
       t.TEMPLATECODE,
       t.ORDERTYPE,
       t.PROVISIONALCOUNTERCODE,
       t.PROVISIONALCODE,
       t.PROVISIONALDOCUMENTDATE,
       t.DEFDOCIDREQ
FROM   DB2ADMIN.SALESDOCUMENTIMPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
