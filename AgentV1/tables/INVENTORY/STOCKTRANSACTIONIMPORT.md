# DB2ADMIN.STOCKTRANSACTIONIMPORT

- **Module**: `INVENTORY` (high confidence — table name starts with 'STOCK')
- **Roles**: `business_data`
- **Columns**: 108
- **Primary key**: `COMPANYCODE`, `TRANSACTIONNUMBER`, `TRANSACTIONDETAILNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 28057

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `TRANSACTIONNUMBER` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `NOWTRNNUMBERTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 4 | `TRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `TRANSACTIONSTATUS` | CHAR(2) |  |  |  |  |
| 6 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `TRANSACTIONDATE` | DATE |  |  |  |  |
| 8 | `TRANSACTIONTIME` | TIME |  |  |  |  |
| 9 | `DETAILTYPE` | CHAR(2) |  |  |  |  |
| 10 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 11 | `STOCKTRANSACTIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `DECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 13 | `DECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 14 | `DECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 15 | `DECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 16 | `DECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 17 | `DECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 18 | `DECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 19 | `DECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 20 | `DECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 21 | `DECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 22 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 23 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 24 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 25 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 27 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 28 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 29 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 30 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 31 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 32 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 33 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 34 | `DERIVATIONCODE` | CHAR(15) |  |  |  |  |
| 35 | `DERIVATIONLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 36 | `DERIVATIONCOMPONENTLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 37 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 38 | `QUALITYREASONCODE` | CHAR(3) |  |  |  |  |
| 39 | `FIRSTQUALITYCONTROLDATE` | DATE |  |  |  |  |
| 40 | `FIRSTQUALITYCONTROLCOUNTER` | CHAR(8) |  |  |  |  |
| 41 | `FIRSTQUALITYCONTROLNUMBER` | CHAR(15) |  |  |  |  |
| 42 | `PHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 43 | `WHSLOCATIONWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 44 | `WAREHOUSELOCATIONCODE` | CHAR(10) |  |  |  |  |
| 45 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 46 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 47 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 48 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 49 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 50 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 51 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 52 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 53 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 54 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 55 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 56 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 57 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 58 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 59 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 60 | `BILLDATE` | DATE |  |  |  |  |
| 61 | `BILLTYPE` | SMALLINT | NOT NULL |  |  |  |
| 62 | `BILLCOUNTER` | CHAR(8) |  |  |  |  |
| 63 | `BILLCODE` | CHAR(50) |  |  |  |  |
| 64 | `INTERNALDOCUMENTDATE` | DATE |  |  |  |  |
| 65 | `INTERNALDOCUMENTNUMBER` | INTEGER | NOT NULL |  |  |  |
| 66 | `ORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 67 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 68 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 69 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 70 | `ORDERCOMPONENTLINE` | DECIMAL(3,0) |  |  |  |  |
| 71 | `ORDERDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 72 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 73 | `RETURNCODE` | CHAR(15) |  |  |  |  |
| 74 | `RETURNLINE` | DECIMAL(7,0) |  |  |  |  |
| 75 | `TOKENCODE` | CHAR(20) |  |  |  |  |
| 76 | `ADUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 77 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 78 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 79 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 80 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 81 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 82 | `TEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 83 | `DECOCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 84 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 85 | `QUALITYLVLITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 86 | `QUALITYREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 87 | `PHYSICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 88 | `WHSLOCWHSZONEPHYWHSCMYCODE` | CHAR(3) |  |  |  |  |
| 89 | `CONTAINERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 90 | `CONTAINERELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 91 | `LOTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 92 | `ITEMELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 93 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 94 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 95 | `ORDERCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 96 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 97 | `AUTOISSUETEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 98 | `AUTOISSUETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 99 | `TRANSFERALLOCATION` | CHAR(2) |  |  |  |  |
| 100 | `ISSUEQTYFROMBALANCE` | SMALLINT | NOT NULL |  |  |  |
| 101 | `ENVCODESKIPBLCEXP` | CHAR(30) |  |  |  |  |
| 102 | `ADUNIQUEIDFORAUTOISSUE` | BIGINT | NOT NULL |  |  |  |
| 103 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 104 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 105 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 106 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 107 | `SUPPLIERLOTCODE` | CHAR(35) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `STOCKTRNIMP1` (ORDERCODE, ORDERCOUNTERCODE)
- `STOCKTRNIMP2` (COMPANYCODE, IMPORTSTATUS, NOWTRNNUMBERTRANSACTIONNUMBER)
- `STOCKTRANSACTIONIMPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.IMPORTSTATUS,
       t.COMPANYCODE,
       t.TRANSACTIONNUMBER,
       t.NOWTRNNUMBERTRANSACTIONNUMBER,
       t.TRANSACTIONDETAILNUMBER,
       t.TRANSACTIONSTATUS,
       t.ITEMTYPECODE,
       t.TRANSACTIONDATE,
       t.TRANSACTIONTIME,
       t.DETAILTYPE,
       t.TEMPLATECODE,
       t.STOCKTRANSACTIONTYPE
FROM   DB2ADMIN.STOCKTRANSACTIONIMPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
