# DB2ADMIN.EXTOPHEADERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `SUBCONTRACTING` (medium confidence — table name starts with 'EXTOP')
- **Roles**: `staging_mirror`
- **Columns**: 115
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 235570

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 5 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 7 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 8 | `ORDERDATE` | DATE |  |  |  |  |
| 9 | `INVOICEORDPRNCSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 10 | `INVOICEORDPRNCSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 11 | `BOMNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 12 | `BOMSUBCODE01` | CHAR(20) |  |  |  |  |
| 13 | `BOMVIRTUALRETURNSUBCODE` | CHAR(30) |  |  |  |  |
| 14 | `BOMSUBCODE02` | CHAR(10) |  |  |  |  |
| 15 | `BOMSUBCODE03` | CHAR(10) |  |  |  |  |
| 16 | `BOMSUBCODE04` | CHAR(10) |  |  |  |  |
| 17 | `BOMSUBCODE05` | CHAR(10) |  |  |  |  |
| 18 | `BOMSUBCODE06` | CHAR(10) |  |  |  |  |
| 19 | `BOMSUBCODE07` | CHAR(10) |  |  |  |  |
| 20 | `BOMSUBCODE08` | CHAR(10) |  |  |  |  |
| 21 | `BOMSUBCODE09` | CHAR(10) |  |  |  |  |
| 22 | `BOMSUBCODE10` | CHAR(10) |  |  |  |  |
| 23 | `BOMSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 24 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 25 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 26 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 27 | `EXTERNALITEM` | CHAR(50) |  |  |  |  |
| 28 | `PROTOTYPEMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 29 | `ENTRYITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 30 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 31 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 32 | `VIRTUALITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 33 | `VIRTUALITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 34 | `DIRTYFIELD` | CHAR(20) |  |  |  |  |
| 35 | `SERVTRTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 36 | `PREVIOUSBASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 37 | `PREVIOUSBASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 38 | `PREVIOUSUSERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 39 | `PREVIOUSUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 40 | `ENTRYUSERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 41 | `ENTRYBASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 42 | `ENTRYUSERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 43 | `USERPRIMARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 44 | `BASEPRIMARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 45 | `USERSECONDARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 46 | `BASESECONDARYUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 47 | `USERPACKAGINGUOMVIRTUALCODE` | CHAR(3) |  |  |  |  |
| 48 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 49 | `EXTENDEDSTATUS` | CHAR(2) |  |  |  |  |
| 50 | `SUPPLIERWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 51 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 52 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 53 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 54 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 55 | `EXTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 56 | `EXTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 57 | `INTERNALREFERENCE` | VARCHAR(200) |  |  |  |  |
| 58 | `INTERNALREFERENCEDATE` | DATE |  |  |  |  |
| 59 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 60 | `DELIVERYDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 61 | `TERMSOFSHIPPINGCODE` | CHAR(2) |  |  |  |  |
| 62 | `TRANSPORTREASONCODE` | CHAR(3) |  |  |  |  |
| 63 | `AREACODE` | CHAR(3) |  |  |  |  |
| 64 | `FIRSTCARRIERTYPE` | CHAR(1) |  |  |  |  |
| 65 | `FIRSTCARRIERCODE` | CHAR(8) |  |  |  |  |
| 66 | `REQUIREDDUEDATE` | DATE |  |  |  |  |
| 67 | `CONFIRMEDDUEDATE` | DATE |  |  |  |  |
| 68 | `SUPPLIERACCEPTED` | SMALLINT | NOT NULL |  |  |  |
| 69 | `SUPPLIERACCEPTANCEDATE` | DATE |  |  |  |  |
| 70 | `PLANNEDPICKUPDATE` | DATE |  |  |  |  |
| 71 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 72 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 73 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 74 | `LINEUSERVALUE` | CHAR(20) |  |  |  |  |
| 75 | `PREVIOUSPRICE` | DECIMAL(18,5) |  |  |  |  |
| 76 | `ORIGINALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 77 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 78 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 79 | `PREVIOUSFREEGIFTTAXDEBIT` | CHAR(1) |  |  |  |  |
| 80 | `FREEGIFTTAXDEBIT` | CHAR(1) |  |  |  |  |
| 81 | `PREVIOUSNETVALUEINCLUDINGTAX` | DECIMAL(18,5) |  |  |  |  |
| 82 | `PREVIOUSTAXABLEINCOMEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 83 | `PREVIOUSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 84 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 85 | `PREVIOUSUSEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 86 | `BANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 87 | `BANKCODE` | CHAR(15) |  |  |  |  |
| 88 | `BANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 89 | `BANKEXTERNALCODE` | CHAR(15) |  |  |  |  |
| 90 | `PREVIOUSCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 91 | `OPPOSITEEXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 92 | `BRANDCODE` | CHAR(8) |  |  |  |  |
| 93 | `BRANDDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 94 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 95 | `PAYMENTMETHODDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 96 | `FIRSTCARRIERDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 97 | `INITIALSCHEDULEDDATETIME` | TIMESTAMP |  |  |  |  |
| 98 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 99 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 100 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 101 | `ABSSHAREDUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 102 | `WFMSTATUSREASONCODE` | CHAR(50) |  |  |  |  |
| 103 | `WFMREMARK` | CLOB(2000000) |  |  |  |  |
| 104 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 105 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 106 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 107 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 108 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 109 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 110 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 111 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 112 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 113 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 114 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EXTOPHEADERBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COUNTERCODE,
       t.CODE,
       t.ORDPRNCUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.ORDERDATE,
       t.INVOICEORDPRNCSMSUPPLIERTYPE,
       t.INVOICEORDPRNCSMSUPPLIERCODE,
       t.BOMNUMBERID
FROM   DB2ADMIN.EXTOPHEADERBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
