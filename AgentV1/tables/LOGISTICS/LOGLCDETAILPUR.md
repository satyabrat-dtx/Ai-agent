# DB2ADMIN.LOGLCDETAILPUR

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 203
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 220369

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `LCNO` | CHAR(35) | NOT NULL |  |  |  |
| 3 | `LCDATE` | DATE | NOT NULL |  |  |  |
| 4 | `LCRECEIVEDDATE` | DATE | NOT NULL |  |  |  |
| 5 | `LCEXPIRYDATE` | DATE | NOT NULL |  |  |  |
| 6 | `LCEXTENSIONDATE` | DATE |  |  |  |  |
| 7 | `LCTRANSFERFLAG` | INTEGER | NOT NULL |  |  |  |
| 8 | `LCTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 10 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 11 | `LCADVISORYBANKIDIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 12 | `LCADVISORYBANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 13 | `LCADVISORYBANKCODE` | CHAR(15) |  |  |  |  |
| 14 | `LCADVISORYBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 15 | `LCADVISORYACCID` | CHAR(30) |  |  |  |  |
| 16 | `LCDRAFTBANKIDIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 17 | `LCDRAFTBANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 18 | `LCDRAFTBANKCODE` | CHAR(15) |  |  |  |  |
| 19 | `LCDRAFTBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 20 | `LCDRAFTACCID` | CHAR(30) |  |  |  |  |
| 21 | `LCREIMBANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 22 | `LCREIMBANKCODE` | CHAR(15) |  |  |  |  |
| 23 | `LCREIMBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 24 | `LCNEGOTIATINGBANKBANKCNYCODE` | CHAR(3) |  |  |  |  |
| 25 | `LCNEGOTIATINGBANKCODE` | CHAR(15) |  |  |  |  |
| 26 | `LCNEGOTIATINGBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 27 | `B2BCOURIERAWBNO` | CHAR(20) |  |  |  |  |
| 28 | `B2BCOURIERAWBDATE` | DATE |  |  |  |  |
| 29 | `BANKREFNO` | CHAR(20) |  |  |  |  |
| 30 | `BANKREFDATE` | DATE |  |  |  |  |
| 31 | `BILLOFEXCHANGEMODE` | INTEGER | NOT NULL |  |  |  |
| 32 | `LIBORINTEREST` | DECIMAL(10,0) |  |  |  |  |
| 33 | `FOBBREAKUP` | INTEGER | NOT NULL |  |  |  |
| 34 | `LCTERMSCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 35 | `LCTERMSCODE` | CHAR(3) |  |  |  |  |
| 36 | `LCCONTRACTTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 37 | `LCCONTRACTTYPECODE` | CHAR(3) |  |  |  |  |
| 38 | `ORDERPRESENT` | INTEGER | NOT NULL |  |  |  |
| 39 | `LCOPENINGPARTYCODE` | CHAR(3) |  |  |  |  |
| 40 | `LCOPENINGBANKBANKCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 41 | `LCOPENINGBANKCODE` | CHAR(15) |  |  |  |  |
| 42 | `LCOPENINGBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 43 | `LEGALNAME1` | VARCHAR(200) |  |  |  |  |
| 44 | `ADDRESSLINE1` | VARCHAR(200) |  |  |  |  |
| 45 | `ADDRESSLINE2` | VARCHAR(200) |  |  |  |  |
| 46 | `ADDRESSLINE3` | VARCHAR(200) |  |  |  |  |
| 47 | `ADDRESSLINE4` | VARCHAR(200) |  |  |  |  |
| 48 | `ADDRESSLINE5` | VARCHAR(200) |  |  |  |  |
| 49 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 50 | `TOWN` | VARCHAR(200) |  |  |  |  |
| 51 | `AREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 52 | `AREACODE` | CHAR(3) |  |  |  |  |
| 53 | `COUNTRYCODE` | CHAR(3) |  |  |  |  |
| 54 | `LCBENEFICIARYTYPE` | CHAR(1) |  |  |  |  |
| 55 | `LCBENEFICIARYCODE` | CHAR(8) |  |  |  |  |
| 56 | `LCBENEFICIARYBANKBANKCNYCODE` | CHAR(3) |  |  |  |  |
| 57 | `LCBENEFICIARYBANKCODE` | CHAR(15) |  |  |  |  |
| 58 | `LCBENEFICIARYBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 59 | `LCBENFLEGALNAME1` | VARCHAR(200) |  |  |  |  |
| 60 | `LCBENFADDRESSLINE1` | VARCHAR(200) |  |  |  |  |
| 61 | `LCBENFADDRESSLINE2` | VARCHAR(200) |  |  |  |  |
| 62 | `LCBENFADDRESSLINE3` | VARCHAR(200) |  |  |  |  |
| 63 | `LCBENFADDRESSLINE4` | VARCHAR(200) |  |  |  |  |
| 64 | `LCBENFADDRESSLINE5` | VARCHAR(200) |  |  |  |  |
| 65 | `LCBENFPOSTALCODE` | CHAR(20) |  |  |  |  |
| 66 | `LCBENFTOWN` | VARCHAR(200) |  |  |  |  |
| 67 | `LCBENFAREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 68 | `LCBENFAREACODE` | CHAR(3) |  |  |  |  |
| 69 | `LCDISCREPANCY1` | VARCHAR(200) |  |  |  |  |
| 70 | `LCDISCREPANCY2` | VARCHAR(200) |  |  |  |  |
| 71 | `LCDISCREPANCY3` | VARCHAR(200) |  |  |  |  |
| 72 | `LCDISCREPANCY4` | VARCHAR(200) |  |  |  |  |
| 73 | `LCDISCREPANCY5` | VARCHAR(200) |  |  |  |  |
| 74 | `FINALAUTHORIZATION` | INTEGER | NOT NULL |  |  |  |
| 75 | `TOLERANCEUOMCODE` | CHAR(3) |  |  |  |  |
| 76 | `TOLERANCEPLUS` | DECIMAL(15,5) |  |  |  |  |
| 77 | `TOLERANCEMINUS` | DECIMAL(15,5) |  |  |  |  |
| 78 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 79 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 80 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 81 | `LCAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 82 | `FOREIGNCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 83 | `LCAMOUNTFOREIGNCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 84 | `AMENDEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 85 | `AGENTSCOMMISION` | DECIMAL(9,5) |  |  |  |  |
| 86 | `BANKCHARGESCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 87 | `BANKCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 88 | `LCREMARK1` | VARCHAR(3000) |  |  |  |  |
| 89 | `LCREMARK2` | VARCHAR(200) |  |  |  |  |
| 90 | `LCREMARK3` | VARCHAR(200) |  |  |  |  |
| 91 | `LCREMARK4` | VARCHAR(200) |  |  |  |  |
| 92 | `LCUTILIZATIONFLAG` | INTEGER | NOT NULL |  |  |  |
| 93 | `LCCLOSEFLAG` | INTEGER | NOT NULL |  |  |  |
| 94 | `LCEXPIRYPLACE` | CHAR(35) | NOT NULL |  |  |  |
| 95 | `LCEXPIRYCOUNTRY` | CHAR(35) | NOT NULL |  |  |  |
| 96 | `LCNOMINATION` | CHAR(35) |  |  |  |  |
| 97 | `LCINSPECTION` | CHAR(35) | NOT NULL |  |  |  |
| 98 | `FINALDESTINATIONCODE` | CHAR(3) |  |  |  |  |
| 99 | `COUNTRYFROMCODE` | CHAR(3) |  |  |  |  |
| 100 | `COUNTRYTOCODE` | CHAR(3) |  |  |  |  |
| 101 | `BUYERSNOTIFYPARTY1CSMSUPTYPE` | CHAR(1) |  |  |  |  |
| 102 | `BUYERSNOTIFYPARTY1CSMSUPCODE` | CHAR(8) |  |  |  |  |
| 103 | `BNP1LEGALNAME1` | VARCHAR(200) |  |  |  |  |
| 104 | `BNP1ADDRESSLINE1` | VARCHAR(200) |  |  |  |  |
| 105 | `BNP1ADDRESSLINE2` | VARCHAR(200) |  |  |  |  |
| 106 | `BNP1ADDRESSLINE3` | VARCHAR(200) |  |  |  |  |
| 107 | `BNP1ADDRESSLINE4` | VARCHAR(200) |  |  |  |  |
| 108 | `BNP1ADDRESSLINE5` | VARCHAR(200) |  |  |  |  |
| 109 | `BNP1POSTALCODE` | CHAR(20) |  |  |  |  |
| 110 | `BNP1AREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 111 | `BNP1AREACODE` | CHAR(3) |  |  |  |  |
| 112 | `BNP1COUNTRYCODE` | CHAR(3) |  |  |  |  |
| 113 | `BUYERSNOTIFYPARTY2CSMSUPTYPE` | CHAR(1) |  |  |  |  |
| 114 | `BUYERSNOTIFYPARTY2CSMSUPCODE` | CHAR(8) |  |  |  |  |
| 115 | `BNP2LEGALNAME1` | VARCHAR(200) |  |  |  |  |
| 116 | `BNP2ADDRESSLINE1` | VARCHAR(200) |  |  |  |  |
| 117 | `BNP2ADDRESSLINE2` | VARCHAR(200) |  |  |  |  |
| 118 | `BNP2ADDRESSLINE3` | VARCHAR(200) |  |  |  |  |
| 119 | `BNP2ADDRESSLINE4` | VARCHAR(200) |  |  |  |  |
| 120 | `BNP2ADDRESSLINE5` | VARCHAR(200) |  |  |  |  |
| 121 | `BNP2POSTALCODE` | CHAR(20) |  |  |  |  |
| 122 | `BNP2AREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 123 | `BNP2AREACODE` | CHAR(3) |  |  |  |  |
| 124 | `BNP2COUNTRYCODE` | CHAR(3) |  |  |  |  |
| 125 | `BUYERSNOTIFYPARTY3CSMSUPTYPE` | CHAR(1) |  |  |  |  |
| 126 | `BUYERSNOTIFYPARTY3CSMSUPCODE` | CHAR(8) |  |  |  |  |
| 127 | `BNP3LEGALNAME1` | VARCHAR(200) |  |  |  |  |
| 128 | `BNP3ADDRESSLINE1` | VARCHAR(200) |  |  |  |  |
| 129 | `BNP3ADDRESSLINE2` | VARCHAR(200) |  |  |  |  |
| 130 | `BNP3ADDRESSLINE3` | VARCHAR(200) |  |  |  |  |
| 131 | `BNP3ADDRESSLINE4` | VARCHAR(200) |  |  |  |  |
| 132 | `BNP3ADDRESSLINE5` | VARCHAR(200) |  |  |  |  |
| 133 | `BNP3POSTALCODE` | CHAR(20) |  |  |  |  |
| 134 | `BNP3AREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 135 | `BNP3AREACODE` | CHAR(3) |  |  |  |  |
| 136 | `BNP3COUNTRYCODE` | CHAR(3) |  |  |  |  |
| 137 | `LCTOLERANCE` | DECIMAL(9,5) |  |  |  |  |
| 138 | `LEGALISATIONREQUIRED` | INTEGER | NOT NULL |  |  |  |
| 139 | `LCDESTINATION` | CHAR(35) |  |  |  |  |
| 140 | `PARTIALSHIPMENTFLAG` | INTEGER | NOT NULL |  |  |  |
| 141 | `TRANSHIPMENTALLOWEDFLAG` | INTEGER | NOT NULL |  |  |  |
| 142 | `MARKEDFREIGHT` | INTEGER | NOT NULL |  |  |  |
| 143 | `LCRESTRICTEDWITH` | CHAR(35) |  |  |  |  |
| 144 | `LCADIVISINGCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 145 | `LASTDATEOFSHIPMENT` | DATE |  |  |  |  |
| 146 | `LCCONFIRMINGBANKBANKCNYCODE` | CHAR(3) |  |  |  |  |
| 147 | `LCCONFIRMINGBANKCODE` | CHAR(15) |  |  |  |  |
| 148 | `LCCONFIRMINGBANKBRANCHCODE` | CHAR(6) |  |  |  |  |
| 149 | `BLCONSIGNEECSMSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 150 | `BLCONSIGNEECSMSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 151 | `BLCONSGNLEGALNAME1` | VARCHAR(200) |  |  |  |  |
| 152 | `BLCONSGNADDRESSLINE1` | VARCHAR(200) |  |  |  |  |
| 153 | `BLCONSGNADDRESSLINE2` | VARCHAR(200) |  |  |  |  |
| 154 | `BLCONSGNADDRESSLINE3` | VARCHAR(200) |  |  |  |  |
| 155 | `BLCONSGNADDRESSLINE4` | VARCHAR(200) |  |  |  |  |
| 156 | `BLCONSGNADDRESSLINE5` | VARCHAR(200) |  |  |  |  |
| 157 | `BLCONSGNPOSTALCODE` | CHAR(20) |  |  |  |  |
| 158 | `BLCONSGNTOWN` | VARCHAR(200) |  |  |  |  |
| 159 | `BLCONSGNAREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 160 | `BLCONSGNAREACODE` | CHAR(3) |  |  |  |  |
| 161 | `BLCONSGNCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 162 | `PORTOFDISCHARGECODE` | CHAR(10) |  |  |  |  |
| 163 | `PORTOFDESTINATIONCODE` | CHAR(10) |  |  |  |  |
| 164 | `MODEOFSHIPMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 165 | `MODEOFSHIPMENTCODE` | CHAR(2) |  |  |  |  |
| 166 | `MASTERLCLCNO` | CHAR(35) |  |  |  |  |
| 167 | `MASTERLCLCDATE` | DATE |  |  |  |  |
| 168 | `ADVANCEPAYMENT` | DECIMAL(18,5) |  |  |  |  |
| 169 | `PROCUREMENT` | CHAR(2) |  |  |  |  |
| 170 | `LCACCUMULATEDAMT` | DECIMAL(18,5) |  |  |  |  |
| 171 | `LCMARGINAMT` | DECIMAL(18,5) |  |  |  |  |
| 172 | `LCAPPLICATIONLCAPPLICATIONNO` | CHAR(35) |  |  |  |  |
| 173 | `LCAPPLICATIONLCAPPLICATIONDATE` | DATE |  |  |  |  |
| 174 | `UTILIZEDAMT` | DECIMAL(18,5) |  |  |  |  |
| 175 | `LCMARGINUTILIZEDAMT` | DECIMAL(18,5) |  |  |  |  |
| 176 | `GLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 177 | `GLCODE` | CHAR(20) |  |  |  |  |
| 178 | `LCSTATUS` | INTEGER | NOT NULL |  |  |  |
| 179 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 180 | `BANKMARGINREFNO` | CHAR(25) |  |  |  |  |
| 181 | `MARGINPAYMENTDATE` | DATE |  |  |  |  |
| 182 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 183 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 184 | `LCCLOSED` | SMALLINT | NOT NULL |  |  |  |
| 185 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 186 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 187 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 188 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 189 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 190 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 191 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 192 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 193 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 194 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 195 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 196 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 197 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 198 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 199 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 200 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 201 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 202 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGLCDETAILPUR.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.LCNO,
       t.LCDATE,
       t.LCRECEIVEDDATE,
       t.LCEXPIRYDATE,
       t.LCEXTENSIONDATE,
       t.LCTRANSFERFLAG,
       t.LCTYPECODE,
       t.TAXTEMPLATETEMPLATETYPE,
       t.TAXTEMPLATECODE,
       t.LCADVISORYBANKIDIDENTIFIER
FROM   DB2ADMIN.LOGLCDETAILPUR t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
