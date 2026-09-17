# DB2ADMIN.LOGCUSTOMINVOICE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 130
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 136197

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `INVOICETYPECODE` | CHAR(3) |  |  |  |  |
| 3 | `CODE` | CHAR(20) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `INVOICEDATE` | DATE |  |  |  |  |
| 5 | `FACTORYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 6 | `FACTORYCODE` | CHAR(8) |  |  |  |  |
| 7 | `CONTRACTNOCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 8 | `CONTRACTNOCODE` | CHAR(15) |  |  |  |  |
| 9 | `CONTRACTDATE` | DATE |  |  |  |  |
| 10 | `EXPORTERCODE` | CHAR(3) |  |  |  |  |
| 11 | `EXPORTERREFNO` | CHAR(15) |  |  |  |  |
| 12 | `BUYERSPOREFNO` | VARCHAR(200) |  |  |  |  |
| 13 | `EXPORTERBANKCODBANKCNYCODE` | CHAR(3) |  |  |  |  |
| 14 | `EXPORTERBANKCODECODE` | CHAR(15) |  |  |  |  |
| 15 | `EXPORTERBANKCODEBRANCHCODE` | CHAR(6) |  |  |  |  |
| 16 | `BUYERSBANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 17 | `BUYERSBANKCODE` | CHAR(15) |  |  |  |  |
| 18 | `BUYERSBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 19 | `COMMERCIALINVOICETYPECODE` | CHAR(3) |  |  |  |  |
| 20 | `COMMERCIALINVOICECODE` | CHAR(20) |  |  |  |  |
| 21 | `CONSIGNEECUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 22 | `CONSIGNEECUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 23 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 24 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 25 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
| 26 | `BUYERIFOTCCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 27 | `BUYERIFOTCCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 28 | `NOTIFYPARTYCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 29 | `NOTIFYPARTYCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 30 | `NOTIFYPARTY2CSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 31 | `NOTIFYPARTY2CSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 32 | `GOODSORIGINCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 33 | `DESTINATIONCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 34 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 35 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 36 | `PRECARRIAGEBY` | CHAR(30) |  |  |  |  |
| 37 | `PLACEOFRECEIPTBYPRECARRIAGE` | CHAR(10) |  |  |  |  |
| 38 | `VESSELFLIGHTNO` | CHAR(35) |  |  |  |  |
| 39 | `PORTOFLOADINGCODE` | CHAR(10) |  |  |  |  |
| 40 | `PORTOFDISCHARGECODE` | CHAR(10) |  |  |  |  |
| 41 | `FINALDESTINATIONCODE` | CHAR(3) |  |  |  |  |
| 42 | `WEIGHTUMCODE` | CHAR(3) |  |  |  |  |
| 43 | `GROSSWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 44 | `NETTWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 45 | `TOTALQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 46 | `TOTALNUMBEROFBALES` | INTEGER | NOT NULL |  |  |  |
| 47 | `SHIPLINECUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 48 | `SHIPLINECUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 49 | `CHACUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 50 | `CHACUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 51 | `FORWARDERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 52 | `FORWARDERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 53 | `ETADATE` | DATE |  |  |  |  |
| 54 | `ETDDATE` | DATE |  |  |  |  |
| 55 | `EXWORKDATE` | DATE |  |  |  |  |
| 56 | `HOUSEAWBBILLNO` | CHAR(15) |  |  |  |  |
| 57 | `HOUSEAWBBILLDATE` | DATE |  |  |  |  |
| 58 | `CATEGORY` | CHAR(30) |  |  |  |  |
| 59 | `ITEMDESCRIPTION` | CHAR(100) |  |  |  |  |
| 60 | `AWBNOCODE` | CHAR(20) |  |  |  |  |
| 61 | `AWBDATE` | DATE |  |  |  |  |
| 62 | `CONTAINERNO` | CHAR(30) |  |  |  |  |
| 63 | `EXPORTSHIPPINGBILLCODE` | CHAR(12) |  |  |  |  |
| 64 | `AR3CODE` | CHAR(20) |  |  |  |  |
| 65 | `AR3EXCISEYEARREGNO` | CHAR(30) |  |  |  |  |
| 66 | `AR3EXCISEYEARCODE` | CHAR(4) |  |  |  |  |
| 67 | `AR3DATE` | DATE |  |  |  |  |
| 68 | `AR4CODE` | CHAR(20) |  |  |  |  |
| 69 | `AR4EXCISEYEARREGNO` | CHAR(30) |  |  |  |  |
| 70 | `AR4EXCISEYEARCODE` | CHAR(4) |  |  |  |  |
| 71 | `AR4DATE` | DATE |  |  |  |  |
| 72 | `IPPOLICYNO` | CHAR(30) |  |  |  |  |
| 73 | `IPPOLICYDATE` | DATE |  |  |  |  |
| 74 | `INSURANCECOMPANY` | CHAR(60) |  |  |  |  |
| 75 | `POLICYPREMIUMRATE` | DECIMAL(18,5) |  |  |  |  |
| 76 | `CUSTOMERPREMIUMRATE` | DECIMAL(18,5) |  |  |  |  |
| 77 | `INSURANCEMARKUP` | DECIMAL(9,5) |  |  |  |  |
| 78 | `FOOTERLINES` | CHAR(100) |  |  |  |  |
| 79 | `ADVANCELICENSEFILENO` | CHAR(15) |  |  |  |  |
| 80 | `ADVANCELICENSEFILEDATE` | DATE |  |  |  |  |
| 81 | `SCHEMETYPECODE` | CHAR(3) |  |  |  |  |
| 82 | `ALCODE` | CHAR(30) |  |  |  |  |
| 83 | `ALAPPLICATIONDATE` | DATE |  |  |  |  |
| 84 | `ADVANCELICENSENO` | CHAR(15) |  |  |  |  |
| 85 | `ADVANCELICENSEDATE` | DATE |  |  |  |  |
| 86 | `DEPBAPPLICATIONCODE` | CHAR(12) |  |  |  |  |
| 87 | `EPCGEPCGAPPLICATIONCODE` | CHAR(30) |  |  |  |  |
| 88 | `EPCGAPPLICATIONDATE` | DATE |  |  |  |  |
| 89 | `EPCGLICENSENO` | CHAR(30) |  |  |  |  |
| 90 | `EPCGLICENSEDATE` | DATE |  |  |  |  |
| 91 | `INVOICECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 92 | `EXCHANGERATEOFCONTRACT` | DECIMAL(28,15) |  |  |  |  |
| 93 | `DBKAPPLICATIONCODE` | CHAR(12) |  |  |  |  |
| 94 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 95 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 96 | `TERMSOFPAYMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 97 | `TERMSOFPAYMENTCODE` | CHAR(3) |  |  |  |  |
| 98 | `FOBDELIVERYTERMSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 99 | `FOBDELIVERYTERMSCODE` | CHAR(3) |  |  |  |  |
| 100 | `LCLCNO` | CHAR(35) |  |  |  |  |
| 101 | `LCLCDATE` | DATE |  |  |  |  |
| 102 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 103 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 104 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 105 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 106 | `ROUNDOFFVALUE` | DECIMAL(18,5) |  |  |  |  |
| 107 | `NETTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 108 | `ROUNDOFFITAXCODE` | CHAR(3) |  |  |  |  |
| 109 | `USEDCOUNTER` | INTEGER | NOT NULL |  |  |  |
| 110 | `POSTINGFLAG` | INTEGER | NOT NULL |  |  |  |
| 111 | `PRINTDATEANDTIME` | TIMESTAMP |  |  |  |  |
| 112 | `PRINTUSER` | CHAR(50) |  |  |  |  |
| 113 | `REPRINTDATEANDTIME` | TIMESTAMP |  |  |  |  |
| 114 | `REPRINTUSER` | CHAR(50) |  |  |  |  |
| 115 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 116 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 117 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 118 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 119 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 120 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 121 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 122 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 123 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 124 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 125 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 126 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 127 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 128 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 129 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGCUSTOMINVOICE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGCUSTOMINVOICELINE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.INVOICETYPECODE,
       t.CODE,
       t.INVOICEDATE,
       t.FACTORYCOMPANYCODE,
       t.FACTORYCODE,
       t.CONTRACTNOCOUNTERCODE,
       t.CONTRACTNOCODE,
       t.CONTRACTDATE,
       t.EXPORTERCODE,
       t.EXPORTERREFNO
FROM   DB2ADMIN.LOGCUSTOMINVOICE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
