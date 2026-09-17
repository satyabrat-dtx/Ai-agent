# DB2ADMIN.LOGFINASSETMASTER

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 133
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 224730

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `COUNTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 3 | `CODE` | CHAR(15) | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 5 | `LOCUGENGROUPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 6 | `LOCUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `LOCATIONCODE` | CHAR(10) |  |  |  |  |
| 8 | `METHODTYPE` | CHAR(2) |  |  |  |  |
| 9 | `NOOFMONTHS` | DECIMAL(20,0) |  |  |  |  |
| 10 | `DEPPRECIATIONRATE` | DECIMAL(18,5) |  |  |  |  |
| 11 | `MAINASSETASSETUGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 12 | `MAINASSETASSETCODE` | CHAR(10) |  |  |  |  |
| 13 | `MAINASSETCODE` | CHAR(15) |  |  |  |  |
| 14 | `REFASSETCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 15 | `REFASSETCODE` | CHAR(15) |  |  |  |  |
| 16 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 17 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 18 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 19 | `TYPEOFASSET` | CHAR(1) | NOT NULL |  |  |  |
| 20 | `PACOUNTERCODE` | CHAR(8) |  |  |  |  |
| 21 | `PACODE` | CHAR(15) |  |  |  |  |
| 22 | `AGUGENGROUPTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 23 | `AGUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 24 | `AGCODE` | CHAR(10) |  |  |  |  |
| 25 | `CAPITALGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 26 | `CAPITALGLCODE` | CHAR(20) |  |  |  |  |
| 27 | `ACCUMDEPRGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 28 | `ACCUMDEPRGLCODE` | CHAR(20) |  |  |  |  |
| 29 | `CURRYEARDEPGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 30 | `CURRYEARDEPGLCODE` | CHAR(20) |  |  |  |  |
| 31 | `RESIDUALVALUE` | DECIMAL(15,5) |  |  |  |  |
| 32 | `RESIDUALAMOUNT` | DECIMAL(15,5) |  |  |  |  |
| 33 | `DATEOFPURCHASE` | DATE |  |  |  |  |
| 34 | `DATEOFASSETREADY` | DATE |  |  |  |  |
| 35 | `DATEOFCAPITALIZATION` | DATE |  |  |  |  |
| 36 | `CCFINBVSPBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 37 | `CCFINBVSPPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 38 | `CCCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 39 | `DEPRATECOMCOMPANYITACT` | CHAR(1) |  |  |  |  |
| 40 | `DEPRATECOMDEPRRATECODE` | CHAR(5) |  |  |  |  |
| 41 | `DEPRATECOMRATE` | DECIMAL(5,2) |  |  |  |  |
| 42 | `DEPRATECOMNOOFMONTH` | DECIMAL(20,0) |  |  |  |  |
| 43 | `DEPRATECOMADDITIONDEPRESIONJOB` | DECIMAL(5,2) |  |  |  |  |
| 44 | `DEPRATECOMDEPRMETHOD` | CHAR(1) |  |  |  |  |
| 45 | `DEPRATECOMEFFECTIVEDATEFROM` | DATE |  |  |  |  |
| 46 | `DEPRATEITCOMPANYITACT` | CHAR(1) |  |  |  |  |
| 47 | `DEPRATEITDEPRRATECODE` | CHAR(5) |  |  |  |  |
| 48 | `DEPRATEITRATE` | DECIMAL(5,2) |  |  |  |  |
| 49 | `DEPRATEITNOOFMONTH` | DECIMAL(20,0) |  |  |  |  |
| 50 | `DEPRATEITADDITIONDEPRESIONJOB` | DECIMAL(5,2) |  |  |  |  |
| 51 | `DEPRATEITDEPRMETHOD` | CHAR(1) |  |  |  |  |
| 52 | `DEPRATEITEFFECTIVEDATEFROM` | DATE |  |  |  |  |
| 53 | `OWNERPLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 54 | `OWNERPLANTCODE` | CHAR(8) |  |  |  |  |
| 55 | `USINGPLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 56 | `USINGPLANTCODE` | CHAR(8) |  |  |  |  |
| 57 | `HYPOTOBANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 58 | `HYPOTOBANKCODE` | CHAR(15) |  |  |  |  |
| 59 | `HYPOTOBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 60 | `HYPOREMARKS` | CHAR(50) |  |  |  |  |
| 61 | `LEASEDASSET` | CHAR(1) |  |  |  |  |
| 62 | `LEASEPARTICULARS` | CHAR(50) |  |  |  |  |
| 63 | `MANUFACTNAME` | CHAR(50) |  |  |  |  |
| 64 | `ASSETMAKE` | CHAR(50) |  |  |  |  |
| 65 | `MODEL` | CHAR(50) |  |  |  |  |
| 66 | `SERIALNO` | CHAR(50) |  |  |  |  |
| 67 | `INSURANCEPOLICYDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 68 | `INSURANCEPOLICYPOLICYNO` | CHAR(30) |  |  |  |  |
| 69 | `INSURANCEPOLICYPOLICYDATE` | DATE |  |  |  |  |
| 70 | `DRAWINGREFERENCE` | CHAR(50) |  |  |  |  |
| 71 | `ROADTAXDETAILS` | CHAR(50) |  |  |  |  |
| 72 | `PHYSICALLCATION` | CHAR(50) |  |  |  |  |
| 73 | `PHYVERIFICATIONDATE` | DATE |  |  |  |  |
| 74 | `LCNODIVISIONCODE` | CHAR(3) |  |  |  |  |
| 75 | `LCNOLCNO` | CHAR(35) |  |  |  |  |
| 76 | `LCNOLCDATE` | DATE |  |  |  |  |
| 77 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 78 | `TRANSACTIONTYPE` | CHAR(1) |  |  |  |  |
| 79 | `PURAGAINSTFCLOAN` | CHAR(1) | NOT NULL |  |  |  |
| 80 | `LOANPARTICULARS` | CHAR(50) |  |  |  |  |
| 81 | `UNITOFMEASUREMENT` | CHAR(50) |  |  |  |  |
| 82 | `QUANTITY` | DECIMAL(10,5) | NOT NULL |  |  |  |
| 83 | `STARTOFDEPRECIATION` | DATE |  |  |  |  |
| 84 | `LASTDEPRECIATION` | DATE |  |  |  |  |
| 85 | `PROCESSTYPE` | CHAR(10) |  |  |  |  |
| 86 | `DATEOFSALE` | DATE |  |  |  |  |
| 87 | `UNDERDEPCAL` | SMALLINT | NOT NULL |  |  |  |
| 88 | `FIRSTGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 89 | `FIRSTUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 90 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 91 | `SECONDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 92 | `SNDUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 93 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 94 | `THIRDGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 95 | `THIRDUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 96 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 97 | `FOURTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 98 | `FRUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 99 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 100 | `FIFTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 101 | `FIFTHUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 102 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 103 | `SIXTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 104 | `SIXTHUGRPUGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 105 | `SIXTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 106 | `SEVENTHGROUPCOMPANY` | CHAR(3) |  |  |  |  |
| 107 | `SEUGRPUGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 108 | `SEVENTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 109 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 110 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 111 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 112 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 113 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 114 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 115 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 116 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 117 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 118 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 119 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 120 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 121 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 122 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 123 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 124 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 125 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 126 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 127 | `ITEMELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 128 | `ITEMELEMENTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 129 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 130 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 131 | `LIFEEFFECTIVEDATE` | DATE |  |  |  |  |
| 132 | `ELIGEBLEFORSHIFT` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGFINASSETMASTER.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COUNTERCOMPANYCODE,
       t.COUNTERCODE,
       t.CODE,
       t.BUSINESSUNITCODE,
       t.LOCUGENGROUPTYPECOMPANYCODE,
       t.LOCUSERGENERICGROUPTYPECODE,
       t.LOCATIONCODE,
       t.METHODTYPE,
       t.NOOFMONTHS,
       t.DEPPRECIATIONRATE,
       t.MAINASSETASSETUGENGRPTYPECODE
FROM   DB2ADMIN.LOGFINASSETMASTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
