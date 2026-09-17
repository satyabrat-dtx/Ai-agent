# DB2ADMIN.LOGCOMMERCIALINVOICE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 143
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 135586

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
| 19 | `CONSIGNEECUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 20 | `CONSIGNEECUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 21 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 22 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 23 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
| 24 | `BUYERIFOTCCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 25 | `BUYERIFOTCCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 26 | `NOTIFYPARTYCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 27 | `NOTIFYPARTYCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 28 | `NOTIFYPARTY2CSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 29 | `NOTIFYPARTY2CSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 30 | `GOODSORIGINCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 31 | `DESTINATIONCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 32 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 33 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 34 | `PRECARRIAGEBY` | CHAR(30) |  |  |  |  |
| 35 | `PLACEOFRECEIPTBYPRECARRIAGE` | CHAR(10) |  |  |  |  |
| 36 | `VESSELFLIGHTNO` | CHAR(35) |  |  |  |  |
| 37 | `PORTOFLOADINGCODE` | CHAR(10) |  |  |  |  |
| 38 | `PORTOFDISCHARGECODE` | CHAR(10) |  |  |  |  |
| 39 | `FINALDESTINATIONCODE` | CHAR(3) |  |  |  |  |
| 40 | `WEIGHTUMCODE` | CHAR(3) |  |  |  |  |
| 41 | `GROSSWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 42 | `NETTWEIGHT` | DECIMAL(18,5) |  |  |  |  |
| 43 | `TOTALQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 44 | `TOTALNUMBEROFBALES` | INTEGER | NOT NULL |  |  |  |
| 45 | `SHIPLINECUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 46 | `SHIPLINECUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 47 | `CHACUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 48 | `CHACUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 49 | `FORWARDERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 50 | `FORWARDERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 51 | `ETADATE` | DATE |  |  |  |  |
| 52 | `ETDDATE` | DATE |  |  |  |  |
| 53 | `EXWORKDATE` | DATE |  |  |  |  |
| 54 | `HOUSEAWBBILLNO` | CHAR(15) |  |  |  |  |
| 55 | `HOUSEAWBBILLDATE` | DATE |  |  |  |  |
| 56 | `CATEGORY` | CHAR(30) |  |  |  |  |
| 57 | `ITEMDESCRIPTION` | CHAR(30) |  |  |  |  |
| 58 | `AWBNOCODE` | CHAR(20) |  |  |  |  |
| 59 | `AWBDATE` | DATE |  |  |  |  |
| 60 | `ORIGINALBILLOFLADINGNO` | CHAR(25) |  |  |  |  |
| 61 | `ORIGINALBILLOFLADINGDATE` | DATE |  |  |  |  |
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
| 72 | `POLPOLICYNO` | CHAR(20) |  |  |  |  |
| 73 | `POLPOLICYDATE` | DATE |  |  |  |  |
| 74 | `IPPOLICYNO` | CHAR(30) |  |  |  |  |
| 75 | `IPPOLICYDATE` | DATE |  |  |  |  |
| 76 | `INSURANCECOMPANY` | CHAR(60) |  |  |  |  |
| 77 | `POLICYPREMIUMRATE` | DECIMAL(18,5) |  |  |  |  |
| 78 | `CUSTOMERPREMIUMRATE` | DECIMAL(18,5) |  |  |  |  |
| 79 | `INSURANCEMARKUP` | DECIMAL(9,5) |  |  |  |  |
| 80 | `FOOTERLINES` | CHAR(100) |  |  |  |  |
| 81 | `ADVANCELICENSEFILENO` | CHAR(15) |  |  |  |  |
| 82 | `ADVANCELICENSEFILEDATE` | DATE |  |  |  |  |
| 83 | `SCHEMETYPECODE` | CHAR(3) |  |  |  |  |
| 84 | `ALCODE` | CHAR(30) |  |  |  |  |
| 85 | `ALAPPLICATIONDATE` | DATE |  |  |  |  |
| 86 | `ADVANCELICENSENO` | CHAR(15) |  |  |  |  |
| 87 | `ADVANCELICENSEDATE` | DATE |  |  |  |  |
| 88 | `DEPBAPPLICATIONCODE` | CHAR(12) |  |  |  |  |
| 89 | `DBKAPPLICATIONCODE` | CHAR(12) |  |  |  |  |
| 90 | `EPCGEPCGAPPLICATIONCODE` | CHAR(30) |  |  |  |  |
| 91 | `EPCGAPPLICATIONDATE` | DATE |  |  |  |  |
| 92 | `EPCGLICENSENO` | CHAR(30) |  |  |  |  |
| 93 | `EPCGLICENSEDATE` | DATE |  |  |  |  |
| 94 | `BRCCODE` | CHAR(15) |  |  |  |  |
| 95 | `BRCDATE` | DATE |  |  |  |  |
| 96 | `BILLOFEXCHANGECODE` | CHAR(12) |  |  |  |  |
| 97 | `INVOICECURRENCYCODE` | CHAR(4) |  |  |  |  |
| 98 | `EXCHANGERATEOFCONTRACT` | DECIMAL(28,15) |  |  |  |  |
| 99 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 100 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 101 | `TERMSOFPAYMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 102 | `TERMSOFPAYMENTCODE` | CHAR(3) |  |  |  |  |
| 103 | `FOBDELIVERYTERMSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 104 | `FOBDELIVERYTERMSCODE` | CHAR(3) |  |  |  |  |
| 105 | `LCLCNO` | CHAR(35) |  |  |  |  |
| 106 | `LCLCDATE` | DATE |  |  |  |  |
| 107 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 108 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 109 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 110 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 111 | `ROUNDOFFVALUE` | DECIMAL(18,5) |  |  |  |  |
| 112 | `NETTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 113 | `ROUNDOFFITAXCODE` | CHAR(3) |  |  |  |  |
| 114 | `USEDCOUNTER` | INTEGER | NOT NULL |  |  |  |
| 115 | `POSTINGFLAG` | INTEGER | NOT NULL |  |  |  |
| 116 | `PRINTDATEANDTIME` | TIMESTAMP |  |  |  |  |
| 117 | `PRINTUSER` | CHAR(50) |  |  |  |  |
| 118 | `REPRINTDATEANDTIME` | TIMESTAMP |  |  |  |  |
| 119 | `REPRINTUSER` | CHAR(50) |  |  |  |  |
| 120 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 121 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 122 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 123 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 124 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 125 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 126 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 127 | `FLAG` | CHAR(15) |  |  |  |  |
| 128 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 129 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 130 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 131 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 132 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 133 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 134 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 135 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 136 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 137 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 138 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 139 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 140 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 141 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 142 | `OTHFINDOCCODE` | CHAR(15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGCOMMERCIALINVOICE.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.
- child `LOGCOMMERCIALINVOICELINE`.`FATHERID` → this table's `ABSUNIQUEID` (high confidence)

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
FROM   DB2ADMIN.LOGCOMMERCIALINVOICE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
