# DB2ADMIN.FINASSETMASTERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `staging_mirror`
- **Columns**: 123
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 181436

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 3 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 5 | `LOCUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 6 | `LOCATIONCODE` | CHAR(10) |  |  |  |  |
| 7 | `MAINASSETASSETUGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 8 | `MAINASSETASSETCODE` | CHAR(10) |  |  |  |  |
| 9 | `MAINASSETCODE` | CHAR(15) |  |  |  |  |
| 10 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 11 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 12 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 13 | `TYPEOFASSET` | CHAR(1) |  |  |  |  |
| 14 | `PACOUNTERCODE` | CHAR(8) |  |  |  |  |
| 15 | `PACODE` | CHAR(15) |  |  |  |  |
| 16 | `AGUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 17 | `AGCODE` | CHAR(10) |  |  |  |  |
| 18 | `CAPITALGLCODE` | CHAR(20) |  |  |  |  |
| 19 | `ACCUMDEPRGLCODE` | CHAR(20) |  |  |  |  |
| 20 | `CURRYEARDEPGLCODE` | CHAR(20) |  |  |  |  |
| 21 | `RESIDUALVALUE` | DECIMAL(15,5) |  |  |  |  |
| 22 | `RESIDUALAMOUNT` | DECIMAL(15,5) |  |  |  |  |
| 23 | `DATEOFPURCHASE` | DATE |  |  |  |  |
| 24 | `DATEOFASSETREADY` | DATE |  |  |  |  |
| 25 | `DATEOFCAPITALIZATION` | DATE |  |  |  |  |
| 26 | `CCFINBVSPBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 27 | `CCFINBVSPPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 28 | `CCCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 29 | `DEPRATECOMCOMPANYITACT` | CHAR(1) |  |  |  |  |
| 30 | `DEPRATECOMDEPRRATECODE` | CHAR(5) |  |  |  |  |
| 31 | `DEPRATECOMRATE` | DECIMAL(5,2) |  |  |  |  |
| 32 | `DEPRATECOMNOOFMONTH` | DECIMAL(20,0) |  |  |  |  |
| 33 | `DEPRATECOMADDITIONDEPRESIONJOB` | DECIMAL(5,2) |  |  |  |  |
| 34 | `DEPRATECOMDEPRMETHOD` | CHAR(1) |  |  |  |  |
| 35 | `DEPRATECOMEFFECTIVEDATEFROM` | DATE |  |  |  |  |
| 36 | `DEPRATEITCOMPANYITACT` | CHAR(1) |  |  |  |  |
| 37 | `DEPRATEITDEPRRATECODE` | CHAR(5) |  |  |  |  |
| 38 | `DEPRATEITRATE` | DECIMAL(5,2) |  |  |  |  |
| 39 | `DEPRATEITNOOFMONTH` | DECIMAL(20,0) |  |  |  |  |
| 40 | `DEPRATEITADDITIONDEPRESIONJOB` | DECIMAL(5,2) |  |  |  |  |
| 41 | `DEPRATEITDEPRMETHOD` | CHAR(1) |  |  |  |  |
| 42 | `DEPRATEITEFFECTIVEDATEFROM` | DATE |  |  |  |  |
| 43 | `OWNERPLANTCODE` | CHAR(8) |  |  |  |  |
| 44 | `USINGPLANTCODE` | CHAR(8) |  |  |  |  |
| 45 | `HYPOTOBANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 46 | `HYPOTOBANKCODE` | CHAR(15) |  |  |  |  |
| 47 | `HYPOTOBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 48 | `HYPOREMARKS` | CHAR(50) |  |  |  |  |
| 49 | `LEASEDASSET` | CHAR(1) |  |  |  |  |
| 50 | `LEASEPARTICULARS` | CHAR(50) |  |  |  |  |
| 51 | `MANUFACTNAME` | CHAR(50) |  |  |  |  |
| 52 | `ASSETMAKE` | CHAR(50) |  |  |  |  |
| 53 | `MODEL` | CHAR(50) |  |  |  |  |
| 54 | `SERIALNO` | CHAR(50) |  |  |  |  |
| 55 | `INSURANCEPOLICYDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 56 | `INSURANCEPOLICYPOLICYNO` | CHAR(30) |  |  |  |  |
| 57 | `INSURANCEPOLICYPOLICYDATE` | DATE |  |  |  |  |
| 58 | `DRAWINGREFERENCE` | CHAR(50) |  |  |  |  |
| 59 | `ROADTAXDETAILS` | CHAR(50) |  |  |  |  |
| 60 | `PHYSICALLCATION` | CHAR(50) |  |  |  |  |
| 61 | `PHYVERIFICATIONDATE` | DATE |  |  |  |  |
| 62 | `LCNOLCNO` | CHAR(35) |  |  |  |  |
| 63 | `LCNOLCDATE` | DATE |  |  |  |  |
| 64 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 65 | `TRANSACTIONTYPE` | CHAR(1) |  |  |  |  |
| 66 | `PURAGAINSTFCLOAN` | CHAR(1) |  |  |  |  |
| 67 | `LOANPARTICULARS` | CHAR(50) |  |  |  |  |
| 68 | `UNITOFMEASUREMENT` | CHAR(50) |  |  |  |  |
| 69 | `QUANTITY` | DECIMAL(10,5) |  |  |  |  |
| 70 | `STARTOFDEPRECIATION` | DATE |  |  |  |  |
| 71 | `LASTDEPRECIATION` | DATE |  |  |  |  |
| 72 | `PROCESSTYPE` | CHAR(10) |  |  |  |  |
| 73 | `DATEOFSALE` | DATE |  |  |  |  |
| 74 | `FIRSTUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 75 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 76 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 77 | `THIRDUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 78 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 79 | `SNDUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 80 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 81 | `FIFTHUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 82 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 83 | `SIXTHUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 84 | `SIXTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 85 | `SEVENTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 86 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 87 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 88 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 89 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 90 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 91 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 92 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 93 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 94 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 95 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 96 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 97 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 98 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 99 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 100 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 101 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 102 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 103 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 104 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 105 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 106 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 107 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 108 | `METHODTYPE` | CHAR(2) |  |  |  |  |
| 109 | `NOOFMONTHS` | DECIMAL(20,0) |  |  |  |  |
| 110 | `DEPPRECIATIONRATE` | DECIMAL(18,5) |  |  |  |  |
| 111 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 112 | `FRUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 113 | `SEUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 114 | `REFASSETCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 115 | `REFASSETCODE` | CHAR(15) |  |  |  |  |
| 116 | `LCNODIVISIONCODE` | CHAR(3) |  |  |  |  |
| 117 | `UNDERDEPCAL` | SMALLINT | NOT NULL |  |  |  |
| 118 | `ITEMELEMENTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 119 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 120 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 121 | `LIFEEFFECTIVEDATE` | DATE |  |  |  |  |
| 122 | `ELIGEBLEFORSHIFT` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINASSETMASTERBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.BUSINESSUNITCODE,
       t.LOCUSERGENERICGROUPTYPECODE,
       t.LOCATIONCODE,
       t.MAINASSETASSETUGENGRPTYPECODE,
       t.MAINASSETASSETCODE,
       t.MAINASSETCODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION
FROM   DB2ADMIN.FINASSETMASTERBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
