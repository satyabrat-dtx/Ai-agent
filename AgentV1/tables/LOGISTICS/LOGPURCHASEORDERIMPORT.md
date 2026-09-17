# DB2ADMIN.LOGPURCHASEORDERIMPORT

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`
- **Columns**: 67
- **Primary key**: `COMPANYCODE`, `IMPORTPROVISIONALCODE`, `LOGTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 20471

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTPROVISIONALCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 3 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 4 | `DOCUMENTTYPETYPE` | CHAR(3) |  |  |  |  |
| 5 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 6 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 7 | `ORDERDATE` | DATE |  |  |  |  |
| 8 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 9 | `LIFECYCLECODE` | CHAR(3) |  |  |  |  |
| 10 | `ALTERNATIVEADDRESSUNIQUEID` | BIGINT |  |  |  |  |
| 11 | `ALTERNATIVEADDRESSCODE` | CHAR(8) |  |  |  |  |
| 12 | `DLVORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 13 | `DLVORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 14 | `DELIVERYPOINTTYPE` | CHAR(2) |  |  |  |  |
| 15 | `INVOICEADDRESSTYPE` | CHAR(2) |  |  |  |  |
| 16 | `DELIVERYPOINTUNIQUEID` | BIGINT |  |  |  |  |
| 17 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 18 | `BUYERCODE` | CHAR(25) |  |  |  |  |
| 19 | `DESCRIPTION` | CHAR(50) |  |  | description |  |
| 20 | `INITIALDATE` | DATE |  |  |  |  |
| 21 | `FINALDATE` | DATE |  |  |  |  |
| 22 | `EXTERNALREFERENCE` | CHAR(50) |  |  |  |  |
| 23 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 24 | `INTERNALREFERENCE` | CHAR(50) |  |  |  |  |
| 25 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 26 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 27 | `STATISTICALGROUPCODE` | CHAR(3) |  |  |  |  |
| 28 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 29 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 30 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 31 | `DELIVERYDESCRIPTION` | CHAR(50) |  |  |  |  |
| 32 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 33 | `SHIPPINGDESCRIPTION` | CHAR(50) |  |  |  |  |
| 34 | `AREACODE` | CHAR(3) |  |  |  |  |
| 35 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 36 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 37 | `SECONDCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 38 | `SECONDCARRIERCODE` | CHAR(8) |  |  |  |  |
| 39 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 40 | `REQUIREDDUEDATE` | DATE |  |  |  |  |
| 41 | `CONFIRMEDDUEDATE` | DATE |  |  |  |  |
| 42 | `RELEASETYPE` | CHAR(2) |  |  |  |  |
| 43 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 44 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 45 | `ENTRYEXCHANGERATE` | DECIMAL(15,7) |  |  |  |  |
| 46 | `CONDITIONRETRIEVINGDATE` | DATE |  |  |  |  |
| 47 | `PRCANDDISCOUNTAPPLICATIONTYPE` | CHAR(2) |  |  |  |  |
| 48 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 49 | `PAYMENTSTARTINGDATE` | DATE |  |  |  |  |
| 50 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 51 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 52 | `BANKCODE` | CHAR(5) |  |  |  |  |
| 53 | `BANKBRANCHCODE` | CHAR(5) |  |  |  |  |
| 54 | `BANKBRANCHDESCRIPTION` | CHAR(50) |  |  |  |  |
| 55 | `BANKEXTERNALCODE` | CHAR(5) |  |  |  |  |
| 56 | `INVOICEORDPRNCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 57 | `INVOICEORDPRNCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 58 | `INVOICEADDRESSUNIQUEID` | BIGINT |  |  |  |  |
| 59 | `INVOICEADDRESSCODE` | CHAR(8) |  |  |  |  |
| 60 | `CURRENTSTATUS` | CHAR(2) |  |  |  |  |
| 61 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 62 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 63 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 64 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 65 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 66 | `LOGUSER` | CHAR(25) |  |  | audit | User responsible for the audited change (change-log table). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTPROVISIONALCODE,
       t.TEMPLATECODE,
       t.ORDERTYPE,
       t.DOCUMENTTYPETYPE,
       t.COUNTERCODE,
       t.CODE,
       t.ORDERDATE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.LIFECYCLECODE,
       t.ALTERNATIVEADDRESSUNIQUEID,
       t.ALTERNATIVEADDRESSCODE
FROM   DB2ADMIN.LOGPURCHASEORDERIMPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
